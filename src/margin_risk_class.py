import pandas      as pd
from   math        import sqrt, isnan
from   scipy.stats import norm
from   copy        import deepcopy

from . import utils
from . import wnc
from .agg_sensitivities import (
    k_delta, 
    k_vega, 
    k_curvature
)
from . import (
    dict_margin_by_risk_class,
    dict_margin_by_risk_class,
    list_rates,
    list_fx,
    list_credit_nonQ,
    list_creditQ,
    list_equity,
    list_commodity,
)

class MarginByRiskClass:
    def __init__(self, crif, calculation_currency):
        self.crif    = crif
        self.results = dict_margin_by_risk_class
        self.calculation_currency = calculation_currency
        self.list_risk_types = utils.unique_list(self.crif, 'RiskType')

    # Delta Margin for Rates Risk Classes Only (Risk_IRCurve, Risk_Inflation, Risk_XCcyBasis)
    def IRDeltaMargin(self):
        updates = deepcopy(dict_margin_by_risk_class)

        # Skip any risk types other than rates
        if ('Risk_IRCurve'   not in self.list_risk_types) and \
           ('Risk_Inflation' not in self.list_risk_types) and \
           ('Risk_XCcyBasis' not in self.list_risk_types):
            return pd.DataFrame(updates)

        else:
            dict_CR = {}
            list_K  = []
            list_S  = []

            crif = self.crif[(self.crif['RiskType'].isin(['Risk_IRCurve', 'Risk_Inflation', 'Risk_XCcyBasis']))]
            currency_list = utils.unique_list(crif, 'Qualifier')
            for currency in currency_list:

                list_WS = []
                tenor_K = []
                index   = []

                # CRIF by currency
                crif_currency = crif[(crif['Qualifier'] == currency)]

                # Risk_XCcyBasis is not considered for the concentration risk factor(CR) calculation
                crif_wo_xccybasis = crif_currency.drop(crif_currency[(crif_currency.RiskType == 'Risk_XCcyBasis')].index)

                # Concentration Thresholds
                T  = wnc.T('Rates','Delta',currency=currency)
                CR = utils.concentration_threshold(utils.sum_sensitivities(crif_wo_xccybasis), T)
                dict_CR[currency] = CR

                # Iteration over the rates risk type existing in the CRIF
                list_rates_risk_types = utils.unique_list([risk_class for risk_class in crif_currency['RiskType'] if risk_class in ['Risk_IRCurve', 'Risk_Inflation', 'Risk_XCcyBasis']])
                for risk_class in list_rates_risk_types:

                    # CRIF by risk type
                    crif_risk_class = crif_currency[crif_currency['RiskType'] == risk_class]

                    # Sensitivities Sum
                    sensitivities = utils.sum_sensitivities(crif_risk_class)
                    if risk_class == 'Risk_Inflation':
                        RW = wnc.inflation_rw
                        WS = RW * sensitivities * CR
                        
                        list_WS.append(WS)
                        tenor_K.append('Inf')
                        index.append('Inf')

                    elif risk_class == 'Risk_XCcyBasis':
                        RW = wnc.ccy_basis_swap_spread_rw
                        WS = RW * sensitivities

                        list_WS.append(WS)
                        tenor_K.append('XCcy')
                        index.append('XCcy')

                    elif risk_class == 'Risk_IRCurve':
                        # Mapping sensitivity to tenor k
                        # e.g. 3m: 10000
                        dict_sensitivities = {}

                        # Curve types such as LIBOR3M, OIS, etc
                        subcurve_list = utils.unique_list(crif_risk_class, 'Label2')
                        for subcurve in subcurve_list:
                            # CRIF by curve
                            crif_subcurve = crif_risk_class[crif_risk_class['Label2']==subcurve]

                            dict_sensitivities_tenor = {}
                            # Iteration over tenors
                            for tenor in utils.tenor_list(crif_subcurve):
                                # CRIF by tenor
                                crif_tenor = crif_subcurve[crif_subcurve['Label1']==tenor]
                                
                                # Sensitivities by tenor
                                dict_sensitivities_tenor[tenor] = utils.sum_sensitivities(crif_tenor)
                                dict_sensitivities[subcurve]    = dict_sensitivities_tenor
                                # Ultimately, it is stored like,
                                # {'Libor3m': {'1m': 32, '3m': 64},
                                #  'OIS': {'2Y': 128, '5Y': 256}}

                                #Regular Volatility
                                if currency in wnc.reg_vol_ccy_bucket:
                                    RW = wnc.reg_vol_rw[tenor]
                                #Low Volatility
                                elif currency in wnc.low_vol_ccy_bucket:
                                    RW = wnc.low_vol_rw[tenor]
                                #High Volatility
                                else:
                                    RW = wnc.high_vol_rw[tenor]

                                s  = dict_sensitivities[subcurve][tenor]
                                WS = RW * s * CR

                                list_WS.append(WS)
                                tenor_K.append(tenor)
                                index.append(subcurve)

                K = k_delta('Rates',list_WS,tenor=tenor_K,index=index,calculation_currency=self.calculation_currency)
                list_K.append(K)

                S_b = max(min(sum(list_WS),K),-K)
                list_S.append(S_b)

            K_squared_sum = sum([x**2 for x in list_K])
            for i in range(len(currency_list)):
                for j in range(len(currency_list)):

                    if i == j:
                        continue

                    else:
                        currency_b = currency_list[i]
                        currency_c = currency_list[j]

                        g = min(dict_CR[currency_b], dict_CR[currency_c]) / max(dict_CR[currency_b], dict_CR[currency_c])

                        if len(currency_list) > 1:
                            gamma = wnc.ir_gamma_diff_ccy
                        else:
                            gamma = 1

                        S1 = list_S[i]
                        S2 = list_S[j]

                        K_squared_sum += gamma * S1 * S2 * g

            updates['Rates']['Delta'] += sqrt(K_squared_sum)
            return pd.DataFrame(updates)


    def DeltaMargin(self):
        updates = deepcopy(dict_margin_by_risk_class)

        if (('Risk_FX'         not in self.list_risk_types) and \
            ('Risk_CreditQ'    not in self.list_risk_types) and \
            ('Risk_CreditNonQ' not in self.list_risk_types) and \
            ('Risk_Equity'     not in self.list_risk_types) and \
            ('Risk_Commodity'  not in self.list_risk_types)):
            return pd.DataFrame(updates)

        else:
            allowed_risk_classes = ['Risk_FX','Risk_CreditQ','Risk_CreditNonQ','Risk_Equity','Risk_Commodity']
            list_risk_classes = [risk_class for risk_class in self.list_risk_types if risk_class in allowed_risk_classes]
            for risk_class in list_risk_classes:

                K_Res  = 0
                list_K = []
                list_S = []

                # FX
                if risk_class == 'Risk_FX':
                    list_WS = []
                    list_CR = []
                    crif_fx = self.crif[(self.crif['RiskType']  == risk_class)]

                    currency_list = utils.unique_list(crif_fx, 'Qualifier')

                    for currency in currency_list:
                        crif_currency = crif_fx[crif_fx['Qualifier'] == currency]
                        T = wnc.T(risk_class,'Delta',currency=currency)
                        sensitivities = utils.sum_sensitivities(crif_currency)
                        CR = utils.concentration_threshold(sensitivities,T)
                        list_CR.append(CR)

                        is_given_currency = currency in wnc.high_vol_currency_group
                        is_calc_currency  = self.calculation_currency in wnc.high_vol_currency_group
                        if currency == self.calculation_currency:
                            RW = 0
                        elif (is_given_currency==True) and (is_calc_currency==True):
                            RW  = wnc.fx_rw['High']['High']
                        elif (is_given_currency==True) and (is_calc_currency==False):
                            RW  = wnc.fx_rw['High']['Regular']
                        elif (is_given_currency==False) and (is_calc_currency==True):
                            RW  = wnc.fx_rw['Regular']['High']
                        elif (is_given_currency==False) and (is_calc_currency==False):
                            RW  = wnc.fx_rw['Regular']['Regular']
                        
                        list_WS.append(sensitivities * CR * RW)

                    K = k_delta(risk_class,list_WS,list_CR=list_CR,bucket=currency_list,calculation_currency=self.calculation_currency)
                    updates['FX']['Delta'] += K

                # CreditQ, CreditNonQ, Equity, Commodity
                elif risk_class in ['Risk_CreditQ','Risk_CreditNonQ','Risk_Equity','Risk_Commodity']:

                    crif_others = self.crif[(self.crif['RiskType'] == risk_class)]
                    bucket_list = utils.bucket_list(crif_others)

                    for bucket in bucket_list:
                        if bucket == 0:
                            crif_bucket = crif_others[(crif_others['RiskType'] == risk_class) & (crif_others['Bucket']  == 'Residual')]
                        else:
                            crif_bucket = crif_others[(crif_others['RiskType'] == risk_class) & (crif_others['Bucket'].isin([bucket, str(bucket)]))]

                        # Risk Weight
                        RW = wnc.RW(risk_class, bucket)                         

                        # Concentration Thresholds
                        T = wnc.T(risk_class,'Delta',bucket=bucket)

                        list_WS = []
                        list_CR = []
                        index   = []

                        qualifier_list = utils.unique_list(crif_bucket, 'Qualifier')
                        for qualifier in qualifier_list:
                            crif_qualifier = crif_bucket[crif_bucket['Qualifier'] == qualifier]

                            # Credit
                            if risk_class in ['Risk_CreditQ','Risk_CreditNonQ']:

                                sensitivities_CR = utils.sum_sensitivities(crif_qualifier)
                                CR = max(1,sqrt(abs(sensitivities_CR)/T))

                                list_lable2 = utils.unique_list(crif_qualifier, 'Label2')
                                for label2 in list_lable2:
                                    crif_label2 = crif_qualifier[crif_qualifier['Label2'] == label2]

                                    for tenor in utils.tenor_list(crif_qualifier):
                                        crif_tenor = crif_label2[crif_label2['Label1'] == tenor]
                                        sensitivities = utils.sum_sensitivities(crif_tenor)

                                        list_WS.append(RW * sensitivities * CR)
                                        list_CR.append(CR)

                                        if bucket == 0:
                                            index.append('Res')

                                        else:
                                            if risk_class == 'Risk_CreditQ':
                                                index.append(qualifier)

                                            elif risk_class == 'Risk_CreditNonQ':
                                                index.append(label2)

                            # Equity, Commodity
                            elif risk_class in ['Risk_Equity','Risk_Commodity']:
                                sensitivities_EQCO = utils.sum_sensitivities(crif_qualifier)
                                CR = max(1,sqrt(abs(sensitivities_EQCO)/T))
                                list_CR.append(CR)
                                list_WS.append(RW * sensitivities_EQCO * CR)

                        K = k_delta(risk_class,list_WS,list_CR=list_CR,bucket=bucket,index=index,calculation_currency=self.calculation_currency)

                        if bucket == 0:
                            K_Res += K
                        else:
                            list_K.append(K)
                            S_b = max(min(sum(list_WS),K),-K)
                            list_S.append(S_b)

                    if 0 in bucket_list:
                        bucket_list.remove(0)

                if risk_class == 'Risk_FX':
                    pass

                else:
                    K_squared_sum = sum([x**2 for x in list_K])
                    for i, _ in enumerate(bucket_list):
                        for j, _ in enumerate(bucket_list):

                            if i == j:
                                continue

                            else:
                                bucket1 = bucket_list[i]
                                bucket2 = bucket_list[j]

                                if risk_class in list_rates:
                                    g = min(list_CR)/max(list_CR)

                                    if len(self.currency_list()) > 1:
                                        gamma = wnc.ir_gamma_diff_ccy
                                    else:
                                        gamma = 1

                                elif risk_class in list_fx:
                                    g = 1
                                    gamma = wnc.FX_Corr[4]

                                elif risk_class in list_credit_nonQ:
                                    g = 1
                                    gamma = wnc.gamma(risk_class)

                                else:
                                    g = 1
                                    gamma = wnc.gamma(risk_class,str(bucket1),str(bucket2))

                                S1 = list_S[i]
                                S2 = list_S[j]
                                K_squared_sum += gamma * S1 * S2 * g

                if risk_class in list_creditQ:
                    updates['CreditQ']['Delta'] += sqrt(K_squared_sum) + K_Res

                elif risk_class in list_credit_nonQ:
                    updates['CreditNonQ']['Delta'] += sqrt(K_squared_sum) + K_Res

                elif risk_class in list_equity:
                    updates['Equity']['Delta'] += sqrt(K_squared_sum) + K_Res

                elif risk_class in list_commodity:
                    updates['Commodity']['Delta'] += sqrt(K_squared_sum)

        return pd.DataFrame(updates)


    def IRVegaMargin(self):
        updates = deepcopy(dict_margin_by_risk_class)

        list_K   = []
        dict_S   = {}
        dict_VCR = {}

        allowed_risk_classes = [risk_class for risk_class in self.list_risk_types if risk_class in ['Risk_IRVol', 'Risk_InflationVol']]
        if ('Risk_IRVol' not in self.list_risk_types) and \
           ('Risk_InflationVol' not in self.list_risk_types):
           
            return pd.DataFrame(updates)

        else:
            for risk_class in allowed_risk_classes:
                VRW = wnc.ir_vrw
                currency_list = utils.unique_list(self.crif, 'Qualifier')
                for currency in currency_list:

                    crif_currency = self.crif[(self.crif['RiskType'].isin(['Risk_IRVol','Risk_InflationVol'])) & (self.crif['Qualifier'] == currency)]

                    VR    = []
                    index = []
                    sensitivities_CR = utils.sum_sensitivities(crif_currency)

                    VT  = wnc.T('Rates','Vega',currency=currency)
                    VCR = max(1, sqrt(abs(sensitivities_CR)/VT))
                    dict_VCR[currency] = VCR

                    list_rates_risk_types = utils.unique_list([risk_class for risk_class in crif_currency['RiskType'] if risk_class in ['Risk_IRVol','Risk_InflationVol']])
                    for risk_class in list_rates_risk_types:
                        crif_riskClass = crif_currency[crif_currency['RiskType'] == risk_class]           
                    
                        tenor_list = utils.tenor_list(crif_riskClass)
                        for tenor in tenor_list:
                            crif_tenor = crif_riskClass[crif_riskClass['Label1'] == tenor]
                            sensitivities = utils.sum_sensitivities(crif_tenor)

                            VR.append(VRW * sensitivities * VCR)

                            if risk_class == 'Risk_IRVol':
                                index.append(tenor)
                            elif risk_class == 'Risk_InflationVol':
                                index.append('Inf')
                            
                    K = k_vega('Rates',VR,index=index)            
                    list_K.append(K)
                    
                    S = max(min(sum(VR), K), -K)
                    dict_S[currency] = S

                K_squared_sum = sum([K**2 for K in list_K])
                for b in range(len(currency_list)):
                    for c in range(len(currency_list)):

                        if b == c:
                            continue

                        else:
                            currency_b = currency_list[b]
                            currency_c = currency_list[c]
                            g = min(dict_VCR[currency_b], dict_VCR[currency_c]) / max(dict_VCR[currency_b], dict_VCR[currency_c])
                            gamma = wnc.ir_gamma_diff_ccy
                        
                        K_squared_sum += gamma * dict_S[currency_b] * dict_S[currency_c] * g

                updates['Rates']['Vega'] += sqrt(K_squared_sum)
                return pd.DataFrame(updates)


    def VegaMargin(self):
        updates = deepcopy(dict_margin_by_risk_class)
        
        allowed_risk_classes = ['Risk_CreditVol','Risk_CreditVolNonQ','Risk_EquityVol','Risk_CommodityVol','Risk_FXVol']
        list_risk_classes = [risk_class for risk_class in self.list_risk_types if risk_class in allowed_risk_classes]
        for risk_class in list_risk_classes:
                    
            # Index by Bucket 
            K_Res    = 0
            list_K   = []
            list_S   = []
            list_VCR = []
            
            credit    = ['Risk_CreditVol','Risk_CreditVolNonQ']
            equity    = ['Risk_EquityVol']
            commodity = ['Risk_CommodityVol']
            fx        = ['Risk_FXVol']       
            
            # Skip risk_class not in the lists
            if risk_class not in credit + equity + commodity + fx:
                return pd.DataFrame(updates)

            elif risk_class in fx:

                list_VR  = []
                list_VCR = []

                for currency_pair in utils.currencyPair_list(self.crif):              
                # k: currency_pair

                    pair_list = [currency_pair, currency_pair[3:]+currency_pair[:3]]    
                    crif_fx   = self.crif[(self.crif['RiskType']  == risk_class) & (self.crif['Qualifier'].isin(pair_list))]
                    
                    is_currency1 = currency_pair[:3] in wnc.high_vol_currency_group
                    is_currency2 = currency_pair[3:] in wnc.high_vol_currency_group

                    fx_vol_group1 = 'High' if is_currency1 else 'Regular'
                    fx_vol_group2 = 'High' if is_currency2 else 'Regular'

                    RW = wnc.fx_rw[fx_vol_group2][fx_vol_group1]

                    sigma = RW * sqrt(365/14)/norm.ppf(0.99)

                    HVR = wnc.fx_hvr  # Historical Volatility Ratio
                    VRW = wnc.fx_vrw  # Vega Risk Weight

                    VT = wnc.T(risk_class,'Vega',currency=currency_pair) # Vega Concentration Threshold
                    sensitivities = utils.sum_sensitivities(crif_fx)
                    
                    VR_ik = HVR * sigma * sensitivities

                    VCR = max(1,sqrt(abs(VR_ik)/VT))
                    list_VCR.append(VCR)
                    
                    VR_k = VRW * VR_ik * VCR
                    list_VR.append(VR_k)
                    
                K = k_vega(risk_class, list_VR, VCR=list_VCR)                                
                updates['FX']['Vega'] += K
                                            
            # Equity, Commodity, Credit
            elif risk_class in equity + commodity + credit:            
                
                bucket_list = utils.bucket_list(self.crif[(self.crif['RiskType'] == risk_class)])
                
                for bucket in bucket_list:
                    if bucket == 0:
                        crif_others = self.crif[(self.crif['RiskType'] == risk_class) & (self.crif['Bucket']  == 'Residual')]
                    else:
                        crif_others = self.crif[(self.crif['RiskType'] == risk_class) & (self.crif['Bucket'].isin([bucket, str(bucket)]))]
                    
                    VR       = []
                    list_VCR = []
                    index    = []

                    qualifier_list = utils.unique_list(crif_others, 'Qualifier')
                    for qualifier in qualifier_list:
                        
                        crif_qualifier = crif_others[crif_others['Qualifier'] == qualifier]

                        VR_ik = []
                        RW    = wnc.RW(risk_class,bucket)
                        sigma = RW * sqrt(365/14)/norm.ppf(0.99)

                        if risk_class in equity:
                            HVR = wnc.equity_hvr  # Historical Volatility Ratio

                            if bucket == 12:
                                VRW = wnc.equity_vrw_bucket_12  # Vega Risk Weight
                                
                            else:
                                VRW = wnc.equity_vrw  # Vega Risk Weight

                        elif risk_class in commodity:
                            HVR = wnc.commodity_hvr  # Historical Volatility Ratio
                            VRW = wnc.commodity_vrw  # Vega Risk Weight

                        elif risk_class in credit:                   
                            
                            VT = wnc.T(risk_class,'Vega',bucket=bucket)
                            sensitivities_VT = utils.sum_sensitivities(crif_qualifier)
                            VCR = max(1,sqrt(abs(sensitivities_VT)/VT))
                            
                            list_lable2 = utils.unique_list(list(crif_qualifier['Label2']))
                            for label2 in list_lable2:
                                crif_label2 = crif_qualifier[crif_qualifier['Label2'] == label2]

                                for tenor in utils.tenor_list(crif_qualifier):
                                    crif_tenor = crif_label2[crif_label2['Label1'] == tenor]
                                    sensitivities = utils.sum_sensitivities(crif_tenor)

                                    if risk_class == 'Risk_CreditVol':
                                        VRW = wnc.creditQ_vrw
                                    elif risk_class == 'Risk_CreditVolNonQ':
                                        VRW = wnc.creditNonQ_vrw                        
                                        
                                    VR.append(VRW * sensitivities * VCR)
                                    list_VCR.append(VCR)

                                    if bucket == 0:
                                        index.append('Res')
                                    else:
                                        if risk_class == 'Risk_CreditVol':
                                            index.append(qualifier)
                                        
                                        elif risk_class == 'Risk_CreditVolNonQ':
                                            index.append(label2)
                                    
                        if risk_class in equity + commodity:
                            sensitivities = utils.sum_sensitivities(crif_qualifier)
                            VR_ik.append(HVR * sigma * sensitivities)
                            
                            VR_i = sum(VR_ik)
                            VT   = wnc.T(risk_class,'Vega',bucket=bucket)
                            VCR  = max(1, sqrt(abs(VR_i)/VT))

                            list_VCR.append(VCR)
                            VR.append(VR_i * VRW * VCR)

                            index = ''

                    K = k_vega(risk_class,VR,VCR=list_VCR,bucket=bucket,index=index)

                    if bucket == 0:
                        K_Res += K
                    else:
                        list_K.append(K)
                        S = max(min(sum(VR), K), -K)
                        list_S.append(S)                

                if 0 in bucket_list:
                    bucket_list.remove(0)  

                K_squared_sum = sum([K**2 for K in list_K])
                for i, _ in enumerate(list_S):
                    for j, _ in enumerate(list_S):

                        if i == j:
                            continue

                        else:
                            bucket_i = str(bucket_list[i])
                            bucket_j = str(bucket_list[j])
                            
                            if risk_class == 'Risk_CreditVolNonQ':
                                gamma = wnc.gamma(risk_class)
                            else:
                                gamma = wnc.gamma(risk_class, bucket_i, bucket_j)
                            
                            K_squared_sum += gamma * list_S[i] * list_S[j]
            

                if risk_class in list_creditQ:
                    updates['CreditQ']['Vega'] += sqrt(K_squared_sum) + K_Res 

                elif risk_class in list_credit_nonQ:
                    updates['CreditNonQ']['Vega'] += sqrt(K_squared_sum) + K_Res 

                elif risk_class in list_equity:
                    updates['Equity']['Vega'] += sqrt(K_squared_sum) + K_Res 

                elif risk_class in list_commodity:
                    updates['Commodity']['Vega'] += sqrt(K_squared_sum) + K_Res 

        return pd.DataFrame(updates)


    def IRCurvatureMargin(self):
        updates = deepcopy(dict_margin_by_risk_class)

        if ('Risk_IRVol' not in self.list_risk_types) and ('Risk_InflationVol' not in self.list_risk_types):
            return pd.DataFrame(updates)

        else:
            allowed_risk_classes = [risk_class for risk_class in self.list_risk_types if risk_class in ['Risk_IRVol', 'Risk_InflationVol']]
            for risk_class in allowed_risk_classes:
            
                list_K = []
                list_S = []

                CVR_sum     = 0
                CVR_abs_sum = 0

                currency_list = utils.unique_list(self.crif, 'Qualifier')
                for currency in currency_list:
                    crif_currency = self.crif[(self.crif['RiskType'].isin(['Risk_IRVol','Risk_InflationVol'])) & (self.crif['Qualifier'] == currency)]
                    list_rates_risk_types = utils.unique_list([risk_class for risk_class in list(crif_currency['RiskType']) if risk_class in ['Risk_IRVol','Risk_InflationVol']])
                    
                    index = []
                    CVR_ik = []
                    
                    # Make an exception for Risk_InflationVol
                    if (list_rates_risk_types == ['Risk_InflationVol']) and (crif_currency['AmountUSD'].sum()==0) and (self.calculation_currency==currency):
                        return pd.DataFrame(updates)
                    else:
                        for risk_class in list_rates_risk_types:
                            
                            crif_riskClass = crif_currency[crif_currency['RiskType'] == risk_class]

                            for tenor in utils.unique_list(crif_riskClass, 'Label1'):
                                crif_tenor = crif_riskClass[crif_riskClass['Label1'] == tenor]

                                sensitivities = utils.sum_sensitivities(crif_tenor)

                                CVR = utils.scaling_func(tenor) * sensitivities
                                CVR_ik.append(CVR)
                                CVR_sum += CVR    
                                CVR_abs_sum += abs(CVR)             

                                if risk_class == 'Risk_IRVol':
                                    index.append(tenor)
                                elif risk_class == 'Risk_InflationVol':
                                    index.append('Inf')
                                
                        K = k_curvature('Rates', CVR_ik, index=index)
                        list_K.append(K)

                        S = max(min(sum(CVR_ik), K), -K)
                        list_S.append(S)

                theta  = min(CVR_sum/CVR_abs_sum, 0)
                _lambda = (norm.ppf(0.995)**2 - 1) * (1 + theta) - theta


                K = sum([K**2 for K in list_K])
                for i in range(len(list_S)):
                    for j in range(len(list_S)):
                        if i == j:
                            continue

                        else:
                            gamma = wnc.ir_gamma_diff_ccy
                            K += list_S[i] * list_S[j] * (gamma**2)
                
                HVR = wnc.ir_hvr
                updates['Rates']['Curvature'] += max(CVR_sum + _lambda * sqrt(K), 0) / (HVR**2) 
                return pd.DataFrame(updates)


    def CurvatureMargin(self):
        updates = deepcopy(dict_margin_by_risk_class)
        
        credit    = ['Risk_CreditVol','Risk_CreditVolNonQ']
        equity    = ['Risk_EquityVol']
        commodity = ['Risk_CommodityVol']
        fx        = ['Risk_FXVol']
        
        allowed_risk_classes = [risk_class for risk_class in self.list_risk_types if risk_class in credit + equity + commodity + fx]
        for risk_class in allowed_risk_classes:

            K_Res  = 0
            list_K = []
            list_S = []

            CVR_sum         = 0
            CVR_sum_res     = 0
            CVR_abs_sum     = 0
            CVR_abs_sum_res = 0
            
            crif_risk_class = self.crif[(self.crif['RiskType']==risk_class)]

            # Skip risk_class not in the lists
            if risk_class not in credit + equity + commodity + fx:
                pass

            # Equity, Commodity, Credit
            elif risk_class in credit + equity + commodity:
                bucket_list = utils.bucket_list(self.crif[(self.crif['RiskType']==risk_class)])
                for bucket in bucket_list:
                    if bucket == 0:
                        crif_risk_class = self.crif[(self.crif['RiskType']==risk_class) & (self.crif['Bucket']=='Residual')]
                    else:
                        crif_risk_class = self.crif[(self.crif['RiskType']==risk_class) & (self.crif['Bucket'].isin([bucket, str(bucket)]))]

                    CVR_i = []
                    index = []
                    
                    for qualifier in utils.unique_list(crif_risk_class, 'Qualifier'):
                        
                        crif_qualifier = crif_risk_class[crif_risk_class['Qualifier'] == qualifier]           
                        
                        # tenor_list = utils.unique_list(crif_qualifier, 'Label1')
                        # list_vega  = utils.unique_list(crif_qualifier, 'AmountUSD')
                        tenor_list = crif_qualifier['Label1'].to_list()
                        vega_list  = crif_qualifier['AmountUSD'].to_list()

                        RW    = wnc.RW(risk_class,bucket)
                        sigma = RW * sqrt(365/14)/norm.ppf(0.99)

                        if risk_class in equity + commodity:

                            # No curvature margin for equity with bucket 12
                            if (risk_class in equity) and (bucket == 12):
                                sigma = 0                              
                        
                            CVR_ik = []                 
                            for k, vega in zip(tenor_list,vega_list):
                                CVR_ik.append(utils.scaling_func(k) * sigma * vega)
                            CVR_i.append(sum(CVR_ik))
                            index = ''

                        elif risk_class in credit:

                            list_lable2 = utils.unique_list(crif_qualifier, 'Label2')
                            for label2 in list_lable2:
                                crif_label2 = crif_qualifier[crif_qualifier['Label2'] == label2]

                                for tenor in utils.tenor_list(crif_qualifier):
                                    crif_tenor = crif_label2[crif_label2['Label1'] == tenor]

                                    sensitivities = utils.sum_sensitivities(crif_tenor)

                                    if bucket == 0:
                                        index.append('Res')
                                    else:
                                        if risk_class == 'Risk_CreditVol':
                                            index.append(qualifier)
                                        
                                        elif risk_class == 'Risk_CreditVolNonQ':
                                            index.append(label2)
                                    
                                    CVR_i.append(utils.scaling_func(tenor) * sensitivities)

                    K = k_curvature(risk_class, CVR_i, bucket, index)
                    
                    #  Residual bucket
                    if bucket == 0:
                        K_Res += K             
                        CVR_sum_res     += sum(CVR_i)
                        CVR_abs_sum_res += sum([abs(CVR) for CVR in CVR_i])

                    else:
                        if (risk_class == 'Risk_EquityVol') and (bucket == 12):
                            pass

                        else:
                            list_K.append(K)
                            S = max(min(sum(CVR_i), K), -K)
                            list_S.append(S)
                            CVR_sum     += sum(CVR_i)
                            CVR_abs_sum += sum([abs(CVR) for CVR in CVR_i])

            elif risk_class in fx:
                list_CVR = []
                for currency_pair in utils.currencyPair_list(self.crif):
                    pair_list = [currency_pair, currency_pair[3:]+currency_pair[:3]]
                    df = self.crif[(self.crif['RiskType']  == risk_class) & (self.crif['Qualifier'].isin(pair_list))]
            
                    is_ccy1_high_vol = currency_pair[:3] in wnc.high_vol_currency_group
                    is_ccy2_high_vol = currency_pair[3:] in wnc.high_vol_currency_group

                    fx_vol_group1 = 'High' if is_ccy1_high_vol else 'Regular'
                    fx_vol_group2 = 'High' if is_ccy2_high_vol else 'Regular'

                    RW = wnc.fx_rw[fx_vol_group2][fx_vol_group1]
                                                       
                    sigma = RW * sqrt(365/14)/norm.ppf(0.99)                
                    list_vega  = df['AmountUSD'].to_list()
                    tenor_list = df['Label1'].to_list()

                    CVR = 0
                    for k, vega in zip(tenor_list, list_vega):
                        CVR += utils.scaling_func(k) * sigma * vega
                                     
                    list_CVR.append(CVR)  
                    

                K = k_curvature(risk_class, list_CVR)
                list_K.append(K)

                CVR_sum     += sum([CVR for CVR in list_CVR]) 
                CVR_abs_sum += sum([abs(CVR) for CVR in list_CVR]) 


                theta  = 0 if isnan(CVR_sum/CVR_abs_sum) else min(CVR_sum/CVR_abs_sum, 0)
                _lambda = (norm.ppf(0.995)**2 - 1) * (1 + theta) - theta
                updates['FX']['Curvature'] += max(CVR_sum + _lambda * K, 0)
                
            
            if risk_class in fx:
                pass

            elif (risk_class == 'Risk_EquityVol') and (12 in bucket_list) and (len(bucket_list) == 1):
                pass

            else:
                # Exceptions on _lambda & theta for Residual bucket
                if ( 0 in utils.unique_list(bucket_list) ) and ( len(utils.unique_list(bucket_list)) > 1 ):
                    theta   = min(CVR_sum/CVR_abs_sum, 0)
                    _lambda = (norm.ppf(0.995)**2 - 1) * (1 + theta) - theta

                    theta_res   = min(CVR_sum_res/CVR_abs_sum_res, 0)
                    _lambda_res = (norm.ppf(0.995)**2 - 1) * (1 + theta_res) - theta_res

                elif 0 not in bucket_list:               
                    theta   = min(CVR_sum/CVR_abs_sum, 0)
                    _lambda = (norm.ppf(0.995)**2 - 1) * (1 + theta) - theta

                    theta_res   = 0
                    _lambda_res = 0
                
                elif ( 0 in utils.unique_list(bucket_list) ) and ( len(utils.unique_list(bucket_list)) == 1 ):
                    
                    theta_res  = min(CVR_sum_res/CVR_abs_sum_res, 0)
                    _lambda_res = (norm.ppf(0.995)**2 - 1) * (1 + theta_res) - theta_res
                
                    theta   = 0
                    _lambda = 0
                

                K_squared = sum([K**2 for K in list_K])
                if risk_class not in fx:

                    if 0 in bucket_list:
                        bucket_list.remove(0)

                    for i in range(len(list_S)):
                        for j in range(len(list_S)):

                            if i == j:
                                continue

                            else:  
                                if risk_class in equity + commodity + credit:
                                    bucket_i = str(bucket_list[i])
                                    bucket_j = str(bucket_list[j])

                                    if risk_class == 'Risk_CreditVolNonQ':
                                        gamma = wnc.gamma(risk_class)
                                    else:
                                        gamma = wnc.gamma(risk_class, bucket_i, bucket_j)

                                    K_squared += list_S[i] * list_S[j] * (gamma**2)

                curvature_margin_non_res = max(CVR_sum + _lambda * sqrt(K_squared), 0)
                curvature_margin_res    = max(CVR_sum_res + _lambda_res * K_Res, 0)


                if risk_class in equity:
                    updates['Equity']['Curvature'] += curvature_margin_non_res + curvature_margin_res
                    
                elif risk_class in commodity:
                    updates['Commodity']['Curvature'] += curvature_margin_non_res + curvature_margin_res

                elif risk_class == 'Risk_CreditVol':
                    updates['CreditQ']['Curvature'] += curvature_margin_non_res + curvature_margin_res

                elif risk_class == 'Risk_CreditVolNonQ':
                    updates['CreditNonQ']['Curvature'] += curvature_margin_non_res + curvature_margin_res
            
        return pd.DataFrame(updates)


    def BaseCorrMargin(self):
        updates = deepcopy(dict_margin_by_risk_class)
        crif_base_corr = self.crif[(self.crif['RiskType'] == 'Risk_BaseCorr')]
        list_WS = []

        qualifier_list = utils.unique_list(crif_base_corr, 'Qualifier')
        for qualifier in qualifier_list:
            crif_qualifier = crif_base_corr[crif_base_corr['Qualifier']==qualifier]
            RW = wnc.base_corr_weight
            sensitivities = utils.sum_sensitivities(crif_qualifier)
            WS = RW * sensitivities
            list_WS.append(WS)

        BaseCorr = 0
        for i, _ in enumerate(list_WS):
            for j, _ in enumerate(list_WS):
                if (i == j) or (qualifier[i]==qualifier[j]):
                    rho = 1
                else:
                    rho = wnc.rho('Risk_BaseCorr')

                BaseCorr += list_WS[i]*list_WS[j]*rho

        updates['CreditQ']['BaseCorr'] += sqrt(BaseCorr)
        return pd.DataFrame(updates) 
