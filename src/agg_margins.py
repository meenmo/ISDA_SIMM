import pandas as pd
from math import sqrt

from . import wnc
from . import utils
from . import dict_margin_by_risk_class
from .margin_risk_class import MarginByRiskClass


class SIMM:
    def __init__(self, crif, calculation_currency, exchange_rate):
        self.crif = crif
        self.simm = 0
        self.simm_break_down = pd.DataFrame()
        self.calc_currency = calculation_currency
        self.exchange_rate = exchange_rate
        self.calculate_simm()  
    
    # Margin by six risk classes (IR, FX, Equity, Commodity, CreditQ, Credit Non-Q)
    def simm_risk_class(self,crif):    
        margin = MarginByRiskClass(crif, self.calc_currency)
        df_margin_aggregated = margin.IRDeltaMargin()     \
                             + margin.DeltaMargin()       \
                             + margin.IRVegaMargin()      \
                             + margin.VegaMargin()        \
                             + margin.IRCurvatureMargin() \
                             + margin.CurvatureMargin()   \
                             + margin.BaseCorrMargin()

        dict_margins = df_margin_aggregated.to_dict()

        # BaseCorr only presents in the CreditQ
        for dict_risk_class in dict_margins:
            if dict_risk_class != 'CreditQ':
                del dict_margins[dict_risk_class]['BaseCorr']

        for risk_class in dict_margins:
            for risk_measure in dict_margins[risk_class]:
                dict_margins[risk_class][risk_measure] *= self.exchange_rate
        
        return dict_margins

    # SIMM by product class
    def simm_product(self, product_class):

        crif = self.crif[(self.crif['ProductClass'] == product_class)]
     
        dict_simm_risk_class = {}
        risk_class_list = list(dict_margin_by_risk_class.keys())
        simm_by_risk_class = self.simm_risk_class(crif)
        for risk_class in risk_class_list:
            simm_risk_class = sum(list(simm_by_risk_class[risk_class].values()))        
            dict_simm_risk_class[risk_class] = simm_risk_class

        simm_product = 0
        for i in range(6):
            for j in range(6):
                if i == j:
                    psi = 1
                else:
                    psi = wnc.psi(risk_class_list[i], risk_class_list[j])

                simm_product +=  psi \
                              *  dict_simm_risk_class[risk_class_list[i]] \
                              *  dict_simm_risk_class[risk_class_list[j]]
        
        return sqrt(simm_product)

    # Calculation by product class as a pivot data frame
    def results_product_class(self, product_class):
        crif = self.crif[(self.crif['ProductClass'] == product_class)]
        dict_results = self.simm_risk_class(crif)

        df_main = pd.DataFrame(columns=['Risk Class','Risk Measure', 'SIMM_RiskMeasure'])
        df_risk_class = pd.DataFrame(columns=['Risk Class','SIMM_RiskClass'])
        
        for risk_class in dict_results:
            dic_sensiType = dict_results[risk_class]
            df_local_sensiType = pd.DataFrame(dic_sensiType.items(), columns=['Risk Measure', 'SIMM_RiskMeasure'])
            df_local_sensiType['Risk Class'] = risk_class

            values_list = list(dic_sensiType.values())
            if values_list != [0]*len(values_list):
                df_main = pd.concat([df_main, df_local_sensiType])
                      
            IM_risk_class = sum(list(df_local_sensiType['SIMM_RiskMeasure']))
            df_local_riskType = pd.DataFrame({'Risk Class': [risk_class], 'SIMM_RiskClass': [IM_risk_class]})

            df_local_riskType = df_local_riskType.round(2)
            df_risk_class = pd.concat([df_risk_class, df_local_riskType])
        
        df_main = df_main.round(2)

        df_outerJoin = pd.merge(df_risk_class, df_main, left_on='Risk Class', right_on='Risk Class', how='outer')
        df_outerJoin['Product Class'] = product_class

        return pd.pivot_table(df_outerJoin, index=['Product Class','Risk Class','SIMM_RiskClass','Risk Measure'])
    
    def addon_margin(self):
        crif_factorNotional = self.crif[(self.crif['RiskType'].isin(['Param_AddOnNotionalFactor','Notional']))]
        crif_fixed  = self.crif[self.crif['RiskType']=='Param_AddOnFixedAmount']

        addon = crif_fixed['AmountUSD'].sum()
        qualifier_list = utils.unique_list(crif_factorNotional, 'Qualifier')
        for qualifier in qualifier_list:
            crif_qualifier = crif_factorNotional[crif_factorNotional['Qualifier']==qualifier]
            crif_factor    = crif_qualifier[crif_qualifier['RiskType']=='Param_AddOnNotionalFactor']
            crif_notional  = crif_qualifier[crif_qualifier['RiskType']=='Notional']

            factor   = crif_factor['AmountUSD'].sum()/100
            notional = crif_notional['AmountUSD'].sum()
            addon   += factor * notional
    
        return addon

    def calculate_simm(self):
        addon_ms   = 0  # addon multiplicative scales
        dict_addon = {}
        df_total   = pd.DataFrame()

        for product_class in utils.product_list(self.crif):
            df_prod   = self.results_product_class(product_class)
            simm_prod = self.simm_product(product_class)
            df_prod['SIMM_ProductClass'] = simm_prod           
            
            self.simm += simm_prod
            df_total    = pd.concat([df_total, df_prod])

            if 'Param_ProductClassMultiplier' in utils.unique_list(self.crif, 'RiskType'):
                df_ms = self.crif[self.crif['RiskType'] == 'Param_ProductClassMultiplier']
                df_ms_prod = df_ms[df_ms['Qualifier'] == product_class]
                ms = utils.sum_sensitivities(df_ms_prod) - 1
                addon_ms += simm_prod * ms
            
            dict_addon[product_class] = simm_prod

        addon_margin = round(addon_ms + self.addon_margin(), 2)
        self.simm  += addon_margin

        df_total['SIMM Total'] = self.simm        
        df_total = df_total.round(2)
        
        if abs(addon_margin) > 0:
            df_total['Add-On'] = addon_margin
            df = pd.pivot_table(df_total, index=['SIMM Total','Add-On','Product Class','SIMM_ProductClass','Risk Class','SIMM_RiskClass','Risk Measure'])

        else:
            df = pd.pivot_table(df_total, index=['SIMM Total','Product Class','SIMM_ProductClass','Risk Class','SIMM_RiskClass','Risk Measure'])

        pd.set_option('float_format', '{:f}'.format)
        pd.set_option('float_format', '{:,}'.format)

        self.simm_break_down = df.copy()
        return df
