# The parameters below can be found at https://www.isda.org/a/Pf2gE/ISDA-SIMM-v2.5.pdf

# p.14, 33
## Regular/Low Vol Currency Buckets
reg_vol_ccy_bucket = ['USD', 'EUR', 'GBP', 'CHF', 'AUD', 'NZD', 'CAD', 'SEK', 'NOK', 'DKK', 'HKD', 'KRW', 'SGD', 'TWD']
low_vol_ccy_bucket = ['JPY']

## table1: Risk Weights for Regular/Low/High Vol Currency Bucket Respectively
reg_vol_rw = {
    '2w'  : 115,
    '1m'  : 112,
    '3m'  : 96,
    '6m'  : 74,
    '1y'  : 66,
    '2y'  : 61,
    '3y'  : 56,
    '5y'  : 52,
    '10y' : 53,
    '15y' : 57,
    '20y' : 60,
    '30y' : 66,
}

low_vol_rw = {
    '2w'  : 15, 
    '1m'  : 18, 
    '3m'  : 9,
    '6m'  : 11,
    '1y'  : 13,
    '2y'  : 15,
    '3y'  : 18,
    '5y'  : 20,
    '10y' : 19,
    '15y' : 19,
    '20y' : 20,
    '30y' : 23,
}

high_vol_rw = {
    '2w'  : 119, 
    '1m'  : 93, 
    '3m'  : 80,
    '6m'  : 82,
    '1y'  : 90,
    '2y'  : 92,
    '3y'  : 95,
    '5y'  : 95,
    '10y' : 94,
    '15y' : 108,
    '20y' : 105,
    '30y' : 101,
}

## Risk Weights for Any Currency's Inflation Rate/Cross-Currency Basis Swap Spread
inflation_rw = 63
ccy_basis_swap_spread_rw = 21

# p.14, 34: The Historical Volatility Ratio for the Interest Rate Risk Class
ir_hvr = 0.44

# p.14, 35: The Vega Risk Weight for the Interest Rate Risk Class
ir_vrw = 0.18

# p.15, 36: IR - Correlations
## Correlations for Aggregated Weighted Sensitivities/Risk Exposures
ir_corr = list(
    zip(
        [1.00, 0.74, 0.63, 0.55, 0.45, 0.36, 0.32, 0.28, 0.23, 0.20, 0.18, 0.16],
        [0.74, 1.00, 0.80, 0.69, 0.52, 0.41, 0.35, 0.29, 0.24, 0.18, 0.17, 0.16],
        [0.63, 0.80, 1.00, 0.85, 0.67, 0.53, 0.45, 0.39, 0.32, 0.24, 0.22, 0.22],
        [0.55, 0.69, 0.85, 1.00, 0.83, 0.71, 0.62, 0.54, 0.45, 0.36, 0.35, 0.33],
        [0.45, 0.52, 0.67, 0.83, 1.00, 0.94, 0.86, 0.78, 0.65, 0.58, 0.55, 0.53],
        [0.36, 0.41, 0.53, 0.71, 0.94, 1.00, 0.95, 0.89, 0.78, 0.72, 0.68, 0.67],
        [0.32, 0.35, 0.45, 0.62, 0.86, 0.95, 1.00, 0.96, 0.87, 0.80, 0.77, 0.74],
        [0.28, 0.29, 0.39, 0.54, 0.78, 0.89, 0.96, 1.00, 0.94, 0.89, 0.86, 0.84],
        [0.23, 0.24, 0.32, 0.45, 0.65, 0.78, 0.87, 0.94, 1.00, 0.97, 0.95, 0.94],
        [0.20, 0.18, 0.24, 0.36, 0.58, 0.72, 0.80, 0.89, 0.97, 1.00, 0.98, 0.98],
        [0.18, 0.17, 0.22, 0.35, 0.55, 0.68, 0.77, 0.86, 0.95, 0.98, 1.00, 0.99],
        [0.16, 0.16, 0.22, 0.33, 0.53, 0.67, 0.74, 0.84, 0.94, 0.98, 0.99, 1.00],   
    )
)
## The Correlation between any two sub-curves of the same currency
sub_curves_corr = 0.99
inflation_corr  = 0.37
ccy_basis_spread_corr = 0.01

# p.15, 37: The parameter for aggregating across different currencies
ir_gamma_diff_ccy = 0.24

# p.16, 39: Risk Weights for Credit Qualifying
creditQ_rw = {
    1:  75,
    2:  91,
    3:  78,
    4:  55,
    5:  67,
    6:  47,
    7:  187,
    8:  665,
    9:  262,
    10: 251,
    11: 172,
    12: 247,
    0:  665, # Residual
}

# p.17, 40: Vega Risk Weight for Credit Qualifying
creditQ_vrw = 0.74

# p.17, 41: Base Correlation Weight
base_corr_weight = 10

# p.17, 42: Credit Qualifying Correlations
creditQ_corr = [0.93,0.42,0.5,0.24]

# p.17, 43: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
creditQ_corr_non_res = list(
    zip(
        [1.00, 0.36, 0.38, 0.35, 0.37, 0.33, 0.36, 0.31, 0.32, 0.33, 0.32, 0.30],
        [0.36, 1.00, 0.46, 0.44, 0.45, 0.43, 0.33, 0.36, 0.38, 0.39, 0.40, 0.36],
        [0.38, 0.46, 1.00, 0.49, 0.49, 0.47, 0.34, 0.36, 0.41, 0.42, 0.43, 0.39],
        [0.35, 0.44, 0.49, 1.00, 0.48, 0.48, 0.31, 0.34, 0.38, 0.42, 0.41, 0.37],
        [0.37, 0.45, 0.49, 0.48, 1.00, 0.48, 0.33, 0.35, 0.39, 0.42, 0.43, 0.38],
        [0.33, 0.43, 0.47, 0.48, 0.48, 1.00, 0.29, 0.32, 0.36, 0.39, 0.40, 0.35],
        [0.36, 0.33, 0.34, 0.31, 0.33, 0.29, 1.00, 0.28, 0.32, 0.31, 0.30, 0.28],
        [0.31, 0.36, 0.36, 0.34, 0.35, 0.32, 0.28, 1.00, 0.33, 0.34, 0.33, 0.30],
        [0.32, 0.38, 0.41, 0.38, 0.39, 0.36, 0.32, 0.33, 1.00, 0.38, 0.36, 0.34],
        [0.33, 0.39, 0.42, 0.42, 0.42, 0.39, 0.31, 0.34, 0.38, 1.00, 0.38, 0.36],
        [0.32, 0.40, 0.43, 0.41, 0.43, 0.40, 0.30, 0.33, 0.36, 0.38, 1.00, 0.35],
        [0.30, 0.36, 0.39, 0.37, 0.38, 0.35, 0.28, 0.30, 0.34, 0.36, 0.35, 1.00],
    )
)

# p.18, 46: Risk Weights for Credit Non-Qualifying
creiditNonQ_rw = {
    1: 280,
    2: 1300,
    0: 1300, # Residual
}

# p.18, 47: Vega Risk Weight for Credit Non-Qualifying
creditNonQ_vrw = 0.74

# p.18, 48: Credit Non-Qualifying Correlations
creditNonQ_corr = [0.82,0.27,0.5]

# p.18, 49: Correlation between non-residual bucket
cr_gamma_diff_ccy = 0.40

# p.20, 56: Risk Weights for Equity Risk Class
equity_rw = {
    1:  26,
    2:  28,
    3:  34,
    4:  28,
    5:  23,
    6:  25,
    7:  29,
    8:  27,
    9:  32,
    10: 32,
    11: 18,
    12: 18,
    0:  34, # Residual
}

# p.20, 57: Historical Volatility Ratio for Equity Risk Class
equity_hvr = 0.58

# p.20, 58: Vega Risk Weight for Equity Risk Class 
equity_vrw = 0.45
equity_vrw_bucket_12 = 0.96

# p.20, 59: Correlations for Equity Risk Class
equity_corr = {
    1:  0.18,
    2:  0.23,
    3:  0.30,
    4:  0.26,
    5:  0.23,
    6:  0.35,
    7:  0.36,
    8:  0.33,
    9:  0.19,
    10: 0.20,
    11: 0.45,
    12: 0.45,
    0:  0,   # Residual
}

# p.20, 60: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
equity_corr_non_res = list(
    zip(
        [1.00, 0.20, 0.20, 0.20, 0.13, 0.16, 0.16, 0.16, 0.17, 0.12, 0.18, 0.18],
        [0.20, 1.00, 0.25, 0.23, 0.14, 0.17, 0.18, 0.17, 0.19, 0.13, 0.19, 0.19],
        [0.20, 0.25, 1.00, 0.24, 0.13, 0.17, 0.18, 0.16, 0.20, 0.13, 0.18, 0.18],
        [0.20, 0.23, 0.24, 1.00, 0.17, 0.22, 0.22, 0.22, 0.21, 0.16, 0.24, 0.24],
        [0.13, 0.14, 0.13, 0.17, 1.00, 0.27, 0.26, 0.27, 0.15, 0.20, 0.30, 0.30],
        [0.16, 0.17, 0.17, 0.22, 0.27, 1.00, 0.34, 0.33, 0.18, 0.24, 0.38, 0.38],
        [0.16, 0.18, 0.18, 0.22, 0.26, 0.34, 1.00, 0.32, 0.18, 0.24, 0.37, 0.37],
        [0.16, 0.17, 0.16, 0.22, 0.27, 0.33, 0.32, 1.00, 0.18, 0.23, 0.37, 0.37],
        [0.17, 0.19, 0.20, 0.21, 0.15, 0.18, 0.18, 0.18, 1.00, 0.14, 0.20, 0.20],
        [0.12, 0.13, 0.13, 0.16, 0.20, 0.24, 0.24, 0.23, 0.14, 1.00, 0.25, 0.25],
        [0.18, 0.19, 0.18, 0.24, 0.30, 0.38, 0.37, 0.37, 0.20, 0.25, 1.00, 0.45],
        [0.18, 0.19, 0.18, 0.24, 0.30, 0.38, 0.37, 0.37, 0.20, 0.25, 0.45, 1.00],
    )
)

# p.22, 61: Risk Weights for Commodity Risk Class
commodity_rw = {
    1:  27,
    2:  29,
    3:  33,
    4:  25,
    5:  35,
    6:  24,
    7:  40,
    8:  53,
    9:  44,
    10: 58,
    11: 20,
    12: 21,
    13: 13,
    14: 16,
    15: 13,
    16: 58,
    17: 17,
}

# p.22, 62: Historical Volatility Ratio for Commodity Risk Class
commodity_hvr = 0.69

# p.22, 63: Vega Risk Weight for Commodity Risk Class
commodity_vrw = 0.60

# p.22, 64: Correlations for Commodity Risk Class
commodity_corr = {
    1:  0.84,
    2:  0.98,
    3:  0.96,
    4:  0.97,
    5:  0.98,
    6:  0.88,
    7:  0.98,
    8:  0.49,
    9:  0.80,
    10: 0.46,
    11: 0.55,
    12: 0.46,
    13: 0.66,
    14: 0.18,
    15: 0.21,
    16: 0.00,
    17: 0.36,
}

# p.23, 65: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
commodity_corr_non_res = list(
    zip(
        [1.00, 0.33, 0.21, 0.27, 0.29, 0.21, 0.48, 0.16, 0.41, 0.23, 0.18, 0.02, 0.21, 0.19, 0.15, 0.00, 0.24],
        [0.33, 1.00, 0.94, 0.94, 0.89, 0.21, 0.19, 0.13, 0.21, 0.21, 0.41, 0.27, 0.31, 0.29, 0.21, 0.00, 0.60],
        [0.21, 0.94, 1.00, 0.91, 0.85, 0.12, 0.20, 0.09, 0.19, 0.20, 0.36, 0.18, 0.22, 0.23, 0.23, 0.00, 0.54],
        [0.27, 0.94, 0.91, 1.00, 0.84, 0.14, 0.24, 0.13, 0.21, 0.19, 0.39, 0.25, 0.23, 0.27, 0.18, 0.00, 0.59],
        [0.29, 0.89, 0.85, 0.84, 1.00, 0.15, 0.17, 0.09, 0.16, 0.21, 0.38, 0.28, 0.28, 0.27, 0.18, 0.00, 0.55],
        [0.21, 0.21, 0.12, 0.14, 0.15, 1.00, 0.33, 0.53, 0.26, 0.09, 0.21, 0.04, 0.11, 0.10, 0.09, 0.00, 0.24],
        [0.48, 0.19, 0.20, 0.24, 0.17, 0.33, 1.00, 0.31, 0.72, 0.24, 0.14,-0.12, 0.19, 0.14, 0.08, 0.00, 0.24],
        [0.16, 0.13, 0.09, 0.13, 0.09, 0.53, 0.31, 1.00, 0.24, 0.04, 0.13,-0.07, 0.04, 0.06, 0.01, 0.00, 0.16],
        [0.41, 0.21, 0.19, 0.21, 0.16, 0.26, 0.72, 0.24, 1.00, 0.21, 0.18,-0.07, 0.12, 0.12, 0.10, 0.00, 0.21],
        [0.23, 0.21, 0.20, 0.19, 0.21, 0.09, 0.24, 0.04, 0.21, 1.00, 0.14, 0.11, 0.11, 0.10, 0.07, 0.00, 0.14],
        [0.18, 0.41, 0.36, 0.39, 0.38, 0.21, 0.14, 0.13, 0.18, 0.14, 1.00, 0.28, 0.30, 0.25, 0.18, 0.00, 0.38],
        [0.02, 0.27, 0.18, 0.25, 0.28, 0.04,-0.12,-0.07,-0.07, 0.11, 0.28, 1.00, 0.18, 0.18, 0.08, 0.00, 0.21],
        [0.21, 0.31, 0.22, 0.23, 0.28, 0.11, 0.19, 0.04, 0.12, 0.11, 0.30, 0.18, 1.00, 0.34, 0.16, 0.00, 0.34],
        [0.19, 0.29, 0.23, 0.27, 0.27, 0.10, 0.14, 0.06, 0.12, 0.10, 0.25, 0.18, 0.34, 1.00, 0.13, 0.00, 0.26],
        [0.15, 0.21, 0.23, 0.18, 0.18, 0.09, 0.08, 0.01, 0.10, 0.07, 0.18, 0.08, 0.16, 0.13, 1.00, 0.00, 0.21],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00],
        [0.24, 0.60, 0.54, 0.59, 0.55, 0.24, 0.24, 0.16, 0.21, 0.14, 0.38, 0.21, 0.34, 0.26, 0.21, 0.00, 1.00],
    )
)

# p.24, 67: The group of high FX volatility currencies
high_vol_currency_group = ['BRL', 'RUB', 'TRY', 'ZAR']

# p.24, 69: Risk Weights for a currency depends on the group of the calculation currency
fx_rw = {
    "Regular": {
        "Regular": 7.4,
        "High":    13.6,
    },
    "High": {
        "Regular": 13.6,
        "High":    14.6,
    }
}

# p.24, 70: Historical Volatility Ratio for FX Risk Class
fx_hvr = 0.52

# p.24, 71: Vega Risk Weight for FX Risk Class
fx_vrw = 0.47

# p.24, 72: Correlations for FX
## Regular Vol FX Group
fx_reg_vol_corr = {
    "Regular": {
        "Regular": 0.50,
        "High":    0.27,
    },
    "High": {
        "Regular": 0.27,
        "High":    0.42,
    }
}

# p.25, 72: Correlations for FX Risk Factor
# High Vol FX Group
fx_high_vol_corr = {
    "Regular": {
        "Regular": 0.85,
        "High":    0.54,
    },
    "High": {
        "Regular": 0.54,
        "High":    0.50,
    }
}

# p.25, 73: Correlations for FX Volatility&Curvature Risk Factor
fx_vega_corr = 0.5 

# p.26, 74&75: Delta Concentration Thresholds for Interest Rate Risk
ir_delta_CT = {
    'Others' : 33,  # All other currencies
    'USD'    : 230, # Regular volatility, well-traded 
    'EUR'    : 230, # Regular volatility, well-traded 
    'GBP'    : 230, # Regular volatility, well-traded
    'AUD'    : 44,  # Regular volatility, less well-traded 
    'CAD'    : 44,  # Regular volatility, less well-traded 
    'CHF'    : 44,  # Regular volatility, less well-traded 
    'DKK'    : 44,  # Regular volatility, less well-traded 
    'HKD'    : 44,  # Regular volatility, less well-traded 
    'KRW'    : 44,  # Regular volatility, less well-traded 
    'NOK'    : 44,  # Regular volatility, less well-traded 
    'NZD'    : 44,  # Regular volatility, less well-traded 
    'SEK'    : 44,  # Regular volatility, less well-traded 
    'SGD'    : 44,  # Regular volatility, less well-traded 
    'TWD'    : 44,  # Regular volatility, less well-traded
    'JPY'    : 70, # Low volatility
}

# p.26, 76: Delta Concentration Thresholds for Credit Spread Risk Group
credit_delta_CT = {
    "Qualifying" : {
        1 : 0.91, # Sovereigns including central banks
        2 : 0.19, # Corporate entities 
        3 : 0.19, # Corporate entities
        4 : 0.19, # Corporate entities
        5 : 0.19, # Corporate entities
        6 : 0.19, # Corporate entities
        7 : 0.91, # Sovereigns including central banks
        8 : 0.19, # Corporate entities
        9 : 0.19, # Corporate entities
        10: 0.19, # Corporate entities
        11: 0.19, # Corporate entities
        12: 0.19, # Corporate entities
        0 : 0.19, # Residual
    }, 
    "Non-Qualifying" : {
        1 : 9.5, # Investment Grades(RMBS & CMBS) 
        2 : 0.5, # High Yield/Non-rated (RMBS & CMBS)
        0 : 0.5, # Residual
    }
}

# p.26, 77: Delta Concentration Thresholds for Equity Risk
equity_delta_CT = {
    1 : 10,    # Emerging Markets  - Large Cap
    2 : 10,    # Emerging Markets  - Large Cap
    3 : 10,    # Emerging Markets  - Large Cap
    4 : 10,    # Emerging Markets  - Large Cap
    5 : 21,   # Developed Markets - Large Cap
    6 : 21,   # Developed Markets - Large Cap
    7 : 21,   # Developed Markets - Large Cap
    8 : 21,   # Developed Markets - Large Cap
    9 : 1.4,  # Emerging Markets  - Small Cap
    10: 0.6,  # Developed Markets - Small Cap
    11: 2100, # Indexes, Funds, ETFs, Volatility Indexes
    12: 2100, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 0.6,  # Residual - Not classified
}

# p.27, 78: Delta Concentration Thresholds for Commodity Risk
commodity_delta_CT = {
    1 : 310,  # Coal
    2 : 2100, # Crude Oil
    3 : 1700, # Oil Fractions 
    4 : 1700, # Oil Fractions 
    5 : 1700, # Oil Fractions 
    6 : 3200, # Natural Gas 
    7 : 3200, # Natural Gas 
    8 : 2700, # Power 
    9 : 2700, # Power 
    10: 52,   # Freight, Dry or Wet 
    11: 530,  # Base metals 
    12: 1600, # Precious Metals 
    13: 100,   # Agricultural 
    14: 100,   # Agricultural 
    15: 100,   # Agricultural 
    16: 52,   # Other 
    17: 4000, # Indices 
}

# p.27, 80: Currency Categories
fx_category1 = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CHF', 'CAD'] # Significantly material
fx_category2 = ['BRL', 'CNY', 'HKD', 'INR', 'KRW', 'MXN', 'NOK', 'NZD', 'RUB', 'SEK', 'SGD', 'TRY', 'ZAR'] # Frequently traded

# p.27, 79: Delta Concentration Thresholds for FX Risk
fx_delta_CT = {
    'Category1' : 5100, # Significantly material 
    'Category2' : 1200, # Frequently traded 
    'Others'    : 190,  # All other currencies
}

# p.27, 81: Vega Concentration Thresholds for IR Risk
ir_vega_CT = {
    'Others' : 120,   # All other currencies
    'USD'    : 3300, # Regular volatility, well-traded 
    'EUR'    : 3300, # Regular volatility, well-traded 
    'GBP'    : 3300, # Regular volatility, well-traded
    'AUD'    : 470,  # Regular volatility, less well-traded 
    'CAD'    : 470,  # Regular volatility, less well-traded 
    'CHF'    : 470,  # Regular volatility, less well-traded 
    'DKK'    : 470,  # Regular volatility, less well-traded 
    'HKD'    : 470,  # Regular volatility, less well-traded 
    'KRW'    : 470,  # Regular volatility, less well-traded 
    'NOK'    : 470,  # Regular volatility, less well-traded 
    'NZD'    : 470,  # Regular volatility, less well-traded 
    'SEK'    : 470,  # Regular volatility, less well-traded 
    'SGD'    : 470,  # Regular volatility, less well-traded 
    'TWD'    : 470,  # Regular volatility, less well-traded
    'JPY'    : 570,  # Low volatility
}

# p.27, 83: Vega Concentration Thresholds for Credit Spread Risk
credit_vega_CT = {
    "Qualifying"     : 260, 
    "Non-Qualifying" : 145,
}

# p.28, 84: Vega Concentration Thresholds for Equity Risk
equity_vega_CT = {
    1 : 210,  # Emerging Markets  - Large Cap
    2 : 210,  # Emerging Markets  - Large Cap
    3 : 210,  # Emerging Markets  - Large Cap
    4 : 210,  # Emerging Markets  - Large Cap
    5 : 1300, # Developed Markets - Large Cap
    6 : 1300, # Developed Markets - Large Cap
    7 : 1300, # Developed Markets - Large Cap
    8 : 1300, # Developed Markets - Large Cap
    9 : 40,   # Emerging Markets  - Small Cap
    10: 200,  # Developed Markets - Small Cap
    11: 5900, # Indexes, Funds, ETFs, Volatility Indexes
    12: 5900, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 40,   # Residual - Not classified
}

# p.28, 85: Vega Concentration Thresholds for Commodity Risk
commodity_vega_CT = {
    1 : 210,  # Coal
    2 : 2700, # Crude Oil
    3 : 290,  # Oil Fractions 
    4 : 290,  # Oil Fractions 
    5 : 290,  # Oil Fractions 
    6 : 5000, # Natural Gas 
    7 : 5000, # Natural Gas 
    8 : 920,  # Power 
    9 : 920,  # Power 
    10: 100,  # Freight, Dry or Wet 
    11: 350,  # Base metals 
    12: 720,  # Precious Metals 
    13: 500,  # Agricultural 
    14: 500,  # Agricultural 
    15: 500,  # Agricultural 
    16: 65,   # Other 
    17: 65,   # Indices 
}

# p.28, 86: Vega Concentration Thresholds for FX Risk
fx_vega_CT = {
    'Category1-Category1' : 2800,
    'Category1-Category2' : 1300,
    'Category1-Category3' : 550,
    'Category2-Category2' : 490,
    'Category2-Category3' : 310,
    'Category3-Category3' : 200,
}

# p.29, 88: Correlation between Risk Classes within Product Classes
corr_params = list(
    zip(
        [1.00, 0.29, 0.13, 0.28, 0.46, 0.32],
        [0.29, 1.00, 0.54, 0.71, 0.52, 0.38],
        [0.13, 0.54, 1.00, 0.46, 0.41, 0.12],
        [0.28, 0.71, 0.46, 1.00, 0.49, 0.35],
        [0.46, 0.52, 0.41, 0.49, 1.00, 0.41],
        [0.32, 0.38, 0.12, 0.35, 0.41, 1.00],
    )
)