import pandas as pd

from Weights_and_Corr.v2_7 import *
from . import (
    list_creditQ,
    list_credit_nonQ,
    list_equity,
    list_commodity,
    list_rates,
    list_fx,
    simm_tenor_list
    
)


def RW(risk_class,bucket):
    if risk_class in list_creditQ:
        return creditQ_rw[bucket]
        
    elif risk_class in list_credit_nonQ:
        return creiditNonQ_rw[bucket]

    elif risk_class in list_equity:
        return equity_rw[bucket]

    elif risk_class in list_commodity:
        return commodity_rw[bucket]

def rho(risk_class,index1=None,index2=None,bucket=None):

    if risk_class in list_rates:
        return pd.DataFrame(
            ir_corr,
            columns=simm_tenor_list,
            index=simm_tenor_list
        )[index1][index2]

    elif risk_class in list_creditQ:

        if risk_class == 'Risk_BaseCorr':
            return float(creditQ_corr[3])

        elif (index1 == 'Res') or (index2 == 'Res'):
            rho = creditQ_corr[2]
        elif index1 == index2:
            rho = creditQ_corr[0]
        else:
            rho = creditQ_corr[1]
        return float(rho)

    elif risk_class in list_credit_nonQ:
        if (index1 == 'Res') or (index2 == 'Res'):
            rho = creditNonQ_corr[2]
        elif index1 == index2:
            rho = creditNonQ_corr[0]
        else:
            rho = creditNonQ_corr[1]
        return rho

    elif risk_class in list_equity:
        return equity_corr[bucket]

    elif risk_class in list_commodity:
        return commodity_corr[bucket]

def gamma(risk_class,bucket1=None,bucket2=None):

    if risk_class in list_creditQ:
        bucket_list = [str(i) for i in range(1,13)]
        return pd.DataFrame(
            creditQ_corr_non_res,
            columns=bucket_list,
            index=bucket_list
        )[bucket1][bucket2]

    elif risk_class in list_credit_nonQ:
        return cr_gamma_diff_ccy

    elif risk_class in list_equity:
        bucket_list = [str(i) for i in range(1,13)]
        return pd.DataFrame(
            equity_corr_non_res,
            columns=bucket_list,
            index=bucket_list            
        )[bucket1][bucket2]

    elif risk_class in list_commodity:
        bucket_list = [str(i) for i in range(1,18)] 
        return pd.DataFrame(
            commodity_corr_non_res,
            columns=bucket_list,
            index=bucket_list            
        )[bucket1][bucket2]

def T(risk_class,type,currency=None,bucket=None):
    if type == 'Delta':
        if risk_class == 'Rates':
            try:
                T = ir_delta_CT[currency]
            except KeyError:
                T = ir_delta_CT['Others']

        elif risk_class in list_creditQ:
            T = credit_delta_CT['Qualifying'][bucket]

        elif risk_class in list_credit_nonQ:
            T = credit_delta_CT['Non-Qualifying'][bucket]

        elif risk_class in list_equity:
            T = equity_delta_CT[bucket]                   

        elif risk_class in list_commodity:
            T = commodity_delta_CT[bucket]

        elif risk_class in list_fx:
            if currency in fx_category1:
                T = fx_delta_CT['Category1']
            elif currency in fx_category2:
                T = fx_delta_CT['Category2']
            else:
                T = fx_delta_CT['Others']
         
    elif type == 'Vega':
        if risk_class == 'Rates':
            try:
                T = ir_vega_CT[currency]
            except KeyError:
                T = ir_vega_CT['Others']
                
        elif risk_class in list_creditQ:
            T = credit_vega_CT['Qualifying']

        elif risk_class in list_credit_nonQ:
            T = credit_vega_CT['Non-Qualifying']

        elif risk_class in list_equity:
            T = equity_vega_CT[bucket]         

        elif risk_class in list_commodity:
            T = commodity_vega_CT[bucket]

        elif risk_class in list_fx:
            currency1 = currency[0:3]
            currency2 = currency[3:6]

            if (currency1 in fx_category1) and (currency2 in fx_category1):
                T = fx_vega_CT['Category1-Category1']

            elif ((currency1 in fx_category1) and (currency2 in fx_category2)) or ((currency1 in fx_category2) and (currency2 in fx_category1)):
                T = fx_vega_CT['Category1-Category2']

            elif ((currency1 in fx_category1) and (currency2 not in fx_category1+fx_category2)) or ((currency1 not in fx_category1+fx_category2) and (currency2 in fx_category1)):
                T = fx_vega_CT['Category1-Category3']

            elif (currency1 in fx_category2) and (currency2 in fx_category2):
                T = fx_vega_CT['Category2-Category2']

            elif ((currency1 in fx_category2) and (currency2 not in fx_category1+fx_category2)) or ((currency1 not in fx_category1+fx_category2) and (currency2 in fx_category2)):
                T = fx_vega_CT['Category2-Category3']

            elif (currency1 not in fx_category1+fx_category2) and (currency2 not in fx_category1+fx_category2):
                T = fx_vega_CT['Category3-Category3']

    return T * 1000000

def psi(risk_class1,risk_class2):
    return pd.DataFrame(
        corr_params,
        columns = ['Rates','CreditQ','CreditNonQ','Equity','Commodity','FX'],
        index   = ['Rates','CreditQ','CreditNonQ','Equity','Commodity','FX']
    )[risk_class1][risk_class2]
