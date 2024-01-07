import math
import numpy as np

from . import wnc
from . import (
    list_creditQ,
    list_credit_nonQ,
    list_equity,
    list_commodity,
    list_fx,
)

def k_delta(
        risk_class,
        list_WS,
        list_CR = None,
        bucket  = None,
        tenor   = None,
        index   = None,
        calculation_currency = 'USD'
    ):   

    K = sum([np.array([WS], dtype='double')[0]**2 for WS in list_WS]) # numpy is used due to overflow issue
    for i, _ in enumerate(list_WS):
        for j, _ in enumerate(list_WS):        
            if i == j:
                continue
            else:    
                # Rates
                if risk_class == 'Rates':

                    if (index[i] == index[j]):
                        phi = 1
                    
                    elif (index[i] == 'XCcy') or (index[j] == 'XCcy'):
                        phi = wnc.ccy_basis_spread_corr

                    elif (index[i] == 'Inf') or (index[j] == 'Inf'):
                        phi = wnc.inflation_corr

                    else:
                        phi = wnc.sub_curves_corr

                    if (index[i] not in ['Inf','XCcy']) and (index[j] not in ['Inf','XCcy']):
                        rho = wnc.rho('Risk_IRCurve',tenor[i],tenor[j])

                    else:
                        rho = 1                   
                
                # Credit
                elif risk_class in list_creditQ + list_credit_nonQ:
                    rho = wnc.rho(risk_class,index[i],index[j])
                    
                # Equity, Commodity, FX
                else:
                    if risk_class in list_equity + list_commodity:
                        rho = wnc.rho(risk_class,bucket=bucket)

                    elif risk_class in list_fx:
                                        
                        currency1 = bucket[i]
                        currency2 = bucket[j]

                        is_ccy1_high_vol = currency1 in wnc.high_vol_currency_group
                        is_ccy2_high_vol = currency2 in wnc.high_vol_currency_group

                        if calculation_currency not in wnc.high_vol_currency_group:
                            if (is_ccy1_high_vol==True) and (is_ccy2_high_vol==True):
                                rho = wnc.fx_reg_vol_corr['High']['High']
                            elif (is_ccy1_high_vol==True) and (is_ccy2_high_vol==False):
                                rho = wnc.fx_reg_vol_corr['High']['Regular']
                            elif (is_ccy1_high_vol==False) and (is_ccy2_high_vol==True):
                                rho = wnc.fx_reg_vol_corr['Regular']['High']
                            else:
                                rho = wnc.fx_reg_vol_corr['Regular']['Regular']
                        else:
                            if (is_ccy1_high_vol==True) and (is_ccy2_high_vol==True):
                                rho = wnc.fx_high_vol_corr['High']['High']
                            elif (is_ccy1_high_vol==True) and (is_ccy2_high_vol==False):
                                rho = wnc.fx_high_vol_corr['High']['Regular']
                            elif (is_ccy1_high_vol==False) and (is_ccy2_high_vol==True):
                                rho = wnc.fx_high_vol_corr['Regular']['High']
                            else:
                                rho = wnc.fx_high_vol_corr['Regular']['Regular']
                    
                if risk_class == 'Rates':
                    f = 1
                
                else:
                    f = min(list_CR[i],list_CR[j]) / max(list_CR[i],list_CR[j])
                    phi = 1

                K += rho * list_WS[i] * list_WS[j] * phi * f
    
    return math.sqrt(K)
    

def k_vega(
        risk_class,
        VR,
        VCR    = None,
        bucket = None,
        index  = ''
    ):

    if index == '': # duplicate '' for the iteration
        index = [''] * len(VR)

    K = sum([vr**2 for vr in VR])
    for k, (VR_k, index_k) in enumerate(zip(VR, index)):
        for l, (VR_l, index_l) in enumerate(zip(VR, index)):
            if k == l:
                continue

            else:
                if risk_class == 'Rates':
                    
                    if (index_k == 'Inf') and (index_l == 'Inf'):
                        rho = 1

                    elif (index_k == 'Inf') or (index_l == 'Inf'):
                        rho = wnc.inflation_corr

                    else:
                        rho = wnc.rho('Risk_IRVol', index_k, index_l)

                elif risk_class in list_equity + list_commodity:
                    rho = wnc.rho(risk_class,bucket=bucket)

                elif risk_class in list_fx:
                    rho = wnc.fx_vega_corr

                elif risk_class in ['Risk_CreditVol', 'Risk_CreditVolNonQ']:
                    rho = wnc.rho(risk_class, index_k, index_l)
                    
                if risk_class == 'Rates':
                    f = 1
                else:
                    f = min(VCR[k],VCR[l])/max(VCR[k],VCR[l])
                
                K += f * rho * VR_k * VR_l

    return math.sqrt(K)


def k_curvature(
    risk_class,
    CVR_list,
    bucket = None,
    index  = None
):    

    K = sum([CVR**2 for CVR in CVR_list])      
    for k, _ in enumerate(CVR_list):
        for l, _ in enumerate(CVR_list):

            if k == l:
                continue

            else:
                if risk_class == 'Rates':

                    if (index[k] == 'Inf') and (index[l] == 'Inf'):
                        rho = 1

                    elif (index[k] == 'Inf') or (index[l] == 'Inf'):
                        rho = wnc.inflation_corr

                    else:
                        rho = wnc.rho('Risk_IRVol', index[k], index[l])

                        
                elif risk_class in list_equity + list_commodity:
                    rho = wnc.rho(risk_class,bucket=bucket)
                    
                elif risk_class in list_fx:
                    rho = wnc.fx_vega_corr


                elif risk_class in ['Risk_CreditVol', 'Risk_CreditVolNonQ']:

                    rho = wnc.rho(risk_class, index[k], index[l])

                K += (rho**2) * CVR_list[k] * CVR_list[l]

    return math.sqrt(K)