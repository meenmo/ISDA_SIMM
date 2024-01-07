# The parameters below can be found at https://www.isda.org/a/CeggE/ISDA-SIMM-v2.4-PUBLIC.pdf

# p.14, 33
## Regular/Low Vol Currency Buckets
reg_vol_ccy_bucket = ['USD', 'EUR', 'GBP', 'CHF', 'AUD', 'NZD', 'CAD', 'SEK', 'NOK', 'DKK', 'HKD', 'KRW', 'SGD', 'TWD']
low_vol_ccy_bucket = ['JPY']

## table1: Risk Weights for Regular/Low/High Vol Currency Bucket Respectively
reg_vol_rw = {
    '2w'  : 114,
    '1m'  : 106,
    '3m'  : 95,
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
    '3m'  : 8.6,
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
    '2w'  : 101, 
    '1m'  : 91, 
    '3m'  : 78,
    '6m'  : 80,
    '1y'  : 90,
    '2y'  : 89,
    '3y'  : 94,
    '5y'  : 94,
    '10y' : 92,
    '15y' : 101,
    '20y' : 104,
    '30y' : 102,
}

## Risk Weights for Any Currency's Inflation Rate/Cross-Currency Basis Swap Spread
inflation_rw = 64
ccy_basis_swap_spread_rw = 21

# p.14, 34: The Historical Volatility Ratio for the Interest Rate Risk Class
ir_hvr = 0.44

# p.14, 35: The Vega Risk Weight for the Interest Rate Risk Class
ir_vrw = 0.18

# p.15, 36: IR - Correlations
## Correlations for Aggregated Weighted Sensitivities/Risk Exposures
ir_corr = list(
    zip(
        [1.00, 0.75, 0.63, 0.55, 0.44, 0.35, 0.31, 0.26, 0.21, 0.17, 0.15, 0.14],
        [0.75, 1.00, 0.79, 0.68, 0.51, 0.40, 0.33, 0.28, 0.22, 0.17, 0.15, 0.15],
        [0.63, 0.79, 1.00, 0.85, 0.67, 0.53, 0.45, 0.38, 0.31, 0.23, 0.21, 0.22],
        [0.55, 0.68, 0.85, 1.00, 0.82, 0.70, 0.61, 0.53, 0.44, 0.36, 0.35, 0.33],
        [0.44, 0.51, 0.67, 0.82, 1.00, 0.94, 0.86, 0.78, 0.66, 0.60, 0.58, 0.56],
        [0.35, 0.40, 0.53, 0.70, 0.94, 1.00, 0.96, 0.90, 0.80, 0.75, 0.72, 0.71],
        [0.31, 0.33, 0.45, 0.61, 0.86, 0.96, 1.00, 0.97, 0.88, 0.83, 0.80, 0.78],
        [0.26, 0.28, 0.38, 0.53, 0.78, 0.90, 0.97, 1.00, 0.95, 0.91, 0.88, 0.87],
        [0.21, 0.22, 0.31, 0.44, 0.66, 0.80, 0.88, 0.95, 1.00, 0.97, 0.95, 0.95],
        [0.17, 0.17, 0.23, 0.36, 0.60, 0.75, 0.83, 0.91, 0.97, 1.00, 0.98, 0.98],
        [0.15, 0.15, 0.21, 0.35, 0.58, 0.72, 0.80, 0.88, 0.95, 0.98, 1.00, 0.99],
        [0.14, 0.15, 0.22, 0.33, 0.56, 0.71, 0.78, 0.87, 0.95, 0.98, 0.99, 1.00],   
    )
)
## The Correlation between any two sub-curves of the same currency
sub_curves_corr = 0.986
inflation_corr  = 0.41
ccy_basis_spread_corr = 0.07

# p.15, 37: The parameter for aggregating across different currencies
ir_gamma_diff_ccy = 0.22

# p.16, 39: Risk Weights for Credit Qualifying
creditQ_rw = {
    1:  81,
    2:  96,
    3:  86,
    4:  53,
    5:  59,
    6:  47,
    7:  181,
    8:  452,
    9:  252,
    10: 261,
    11: 218,
    12: 195,
    0:  452, # Residual
}

# p.17, 40: Vega Risk Weight for Credit Qualifying
creditQ_vrw = 0.73

# p.17, 41: Base Correlation Weight
base_corr_weight = 11

# p.17, 42: Credit Qualifying Correlations
creditQ_corr = [0.92,0.41,0.5,0.25]

# p.17, 43: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
creditQ_corr_non_res = list(
    zip(
        [1.00, 0.35, 0.37, 0.35, 0.37, 0.34, 0.38, 0.31, 0.34, 0.33, 0.30, 0.31],
        [0.35, 1.00, 0.44, 0.43, 0.45, 0.42, 0.32, 0.34, 0.38, 0.38, 0.35, 0.35],
        [0.37, 0.44, 1.00, 0.48, 0.49, 0.47, 0.34, 0.35, 0.42, 0.42, 0.40, 0.39],
        [0.35, 0.43, 0.48, 1.00, 0.48, 0.48, 0.32, 0.34, 0.40, 0.41, 0.39, 0.37],
        [0.37, 0.45, 0.49, 0.48, 1.00, 0.48, 0.34, 0.35, 0.41, 0.41, 0.40, 0.39],
        [0.34, 0.42, 0.47, 0.48, 0.48, 1.00, 0.31, 0.33, 0.37, 0.38, 0.38, 0.36],
        [0.38, 0.32, 0.34, 0.32, 0.34, 0.31, 1.00, 0.28, 0.32, 0.30, 0.27, 0.28],
        [0.31, 0.34, 0.35, 0.34, 0.35, 0.33, 0.28, 1.00, 0.32, 0.32, 0.29, 0.29],
        [0.34, 0.38, 0.42, 0.40, 0.41, 0.37, 0.32, 0.32, 1.00, 0.38, 0.35, 0.35],
        [0.33, 0.38, 0.42, 0.41, 0.41, 0.38, 0.30, 0.32, 0.38, 1.00, 0.35, 0.34],
        [0.30, 0.35, 0.40, 0.39, 0.40, 0.38, 0.27, 0.29, 0.35, 0.35, 1.00, 0.33],
        [0.31, 0.35, 0.39, 0.37, 0.39, 0.36, 0.28, 0.29, 0.35, 0.34, 0.33, 1.00],
    )
)

# p.18, 46: Risk Weights for Credit Non-Qualifying
creiditNonQ_rw = {
    1: 280,
    2: 1200,
    0: 1200, # Residual
}

# p.18, 47: Vega Risk Weight for Credit Non-Qualifying
creditNonQ_vrw = 0.73

# p.18, 48: Credit Non-Qualifying Correlations
creditNonQ_corr = [0.86,0.33,0.5]

# p.18, 49: Correlation between non-residual bucket
cr_gamma_diff_ccy = 0.36

# p.20, 56: Risk Weights for Equity Risk Class
equity_rw = {
    1:  25,
    2:  28,
    3:  30,
    4:  28,
    5:  23,
    6:  24,
    7:  29,
    8:  27,
    9:  31,
    10: 33,
    11: 19,
    12: 19,
    0:  33, # Residual
}

# p.20, 57: Historical Volatility Ratio for Equity Risk Class
equity_hvr = 0.54

# p.20, 58: Vega Risk Weight for Equity Risk Class 
equity_vrw = 0.50
equity_vrw_bucket_12 = 0.98

# p.20, 59: Correlations for Equity Risk Class
equity_corr = {
    1:  0.18,
    2:  0.23,
    3:  0.28,
    4:  0.27,
    5:  0.23,
    6:  0.36,
    7:  0.38,
    8:  0.35,
    9:  0.21,
    10: 0.20,
    11: 0.54,
    12: 0.54,
    0:  0,   # Residual
}

# p.20, 60: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
equity_corr_non_res = list(
    zip(
        [1.00, 0.20, 0.21, 0.21, 0.15, 0.19, 0.19, 0.19, 0.18, 0.14, 0.24, 0.24],
        [0.20, 1.00, 0.25, 0.24, 0.16, 0.21, 0.22, 0.21, 0.21, 0.16, 0.27, 0.27],
        [0.21, 0.25, 1.00, 0.26, 0.17, 0.22, 0.24, 0.22, 0.23, 0.17, 0.28, 0.28],
        [0.21, 0.24, 0.26, 1.00, 0.18, 0.24, 0.25, 0.25, 0.23, 0.19, 0.31, 0.31],
        [0.15, 0.16, 0.17, 0.18, 1.00, 0.27, 0.27, 0.27, 0.15, 0.20, 0.32, 0.32],
        [0.19, 0.21, 0.22, 0.24, 0.27, 1.00, 0.36, 0.35, 0.20, 0.25, 0.42, 0.42],
        [0.19, 0.22, 0.24, 0.25, 0.27, 0.36, 1.00, 0.34, 0.20, 0.26, 0.43, 0.43],
        [0.19, 0.21, 0.22, 0.25, 0.27, 0.35, 0.34, 1.00, 0.20, 0.25, 0.41, 0.41],
        [0.18, 0.21, 0.23, 0.23, 0.15, 0.20, 0.20, 0.20, 1.00, 0.16, 0.26, 0.26],
        [0.14, 0.16, 0.17, 0.19, 0.20, 0.25, 0.26, 0.25, 0.16, 1.00, 0.29, 0.29],
        [0.24, 0.27, 0.28, 0.31, 0.32, 0.42, 0.43, 0.41, 0.26, 0.29, 1.00, 0.54],
        [0.24, 0.27, 0.28, 0.31, 0.32, 0.42, 0.43, 0.41, 0.26, 0.29, 0.54, 1.00],
    )
)

# p.22, 61: Risk Weights for Commodity Risk Class
commodity_rw = {
    1:  22,
    2:  29,
    3:  33,
    4:  25,
    5:  35,
    6:  24,
    7:  22,
    8:  49,
    9:  24,
    10: 53,
    11: 20,
    12: 21,
    13: 13,
    14: 15,
    15: 13,
    16: 53,
    17: 17,
}

# p.22, 62: Historical Volatility Ratio for Commodity Risk Class
commodity_hvr = 0.64

# p.22, 63: Vega Risk Weight for Commodity Risk Class
commodity_vrw = 0.61

# p.22, 64: Correlations for Commodity Risk Class
commodity_corr = {
    1:  0.79,
    2:  0.98,
    3:  0.96,
    4:  0.97,
    5:  0.98,
    6:  0.88,
    7:  0.97,
    8:  0.42,
    9:  0.70,
    10: 0.38,
    11: 0.54,
    12: 0.48,
    13: 0.67,
    14: 0.15,
    15: 0.23,
    16: 0.00,
    17: 0.33,
}

# p.23, 65: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
commodity_corr_non_res = list(
    zip(
        [1.00, 0.36, 0.23, 0.30, 0.30, 0.07, 0.32, 0.02, 0.26, 0.20, 0.17, 0.15, 0.21, 0.15, 0.19, 0.00, 0.24],
        [0.36, 1.00, 0.93, 0.94, 0.88, 0.16, 0.21, 0.09, 0.21, 0.20, 0.40, 0.30, 0.24, 0.29, 0.23, 0.00, 0.56],
        [0.23, 0.93, 1.00, 0.91, 0.85, 0.06, 0.21, 0.04, 0.21, 0.19, 0.33, 0.23, 0.14, 0.23, 0.25, 0.00, 0.50],
        [0.30, 0.94, 0.91, 1.00, 0.83, 0.06, 0.24, 0.04, 0.21, 0.17, 0.36, 0.25, 0.14, 0.25, 0.20, 0.00, 0.53],
        [0.30, 0.88, 0.85, 0.83, 1.00, 0.10, 0.17, 0.04, 0.16, 0.17, 0.40, 0.33, 0.25, 0.30, 0.19, 0.00, 0.53],
        [0.07, 0.16, 0.06, 0.06, 0.10, 1.00, 0.27, 0.50, 0.20, 0.04, 0.17, 0.08, 0.12, 0.08, 0.14, 0.00, 0.25],
        [0.32, 0.21, 0.21, 0.24, 0.17, 0.27, 1.00, 0.27, 0.61, 0.18, 0.06,-0.11, 0.12, 0.08, 0.08, 0.00, 0.22],
        [0.02, 0.09, 0.04, 0.04, 0.04, 0.50, 0.27, 1.00, 0.19, 0.00, 0.12,-0.03, 0.09, 0.05, 0.07, 0.00, 0.14],
        [0.26, 0.21, 0.21, 0.21, 0.16, 0.20, 0.61, 0.19, 1.00, 0.14, 0.13,-0.07, 0.07, 0.06, 0.12, 0.00, 0.19],
        [0.20, 0.20, 0.19, 0.17, 0.17, 0.04, 0.18, 0.00, 0.14, 1.00, 0.11, 0.13, 0.07, 0.06, 0.06, 0.00, 0.11],
        [0.17, 0.40, 0.33, 0.36, 0.40, 0.17, 0.06, 0.12, 0.13, 0.11, 1.00, 0.31, 0.27, 0.21, 0.20, 0.00, 0.37],
        [0.15, 0.30, 0.23, 0.25, 0.33, 0.08,-0.11,-0.03,-0.07, 0.13, 0.31, 1.00, 0.15, 0.19, 0.10, 0.00, 0.23],
        [0.21, 0.24, 0.14, 0.14, 0.25, 0.12, 0.12, 0.09, 0.07, 0.07, 0.27, 0.15, 1.00, 0.28, 0.20, 0.00, 0.27],
        [0.15, 0.29, 0.23, 0.25, 0.30, 0.08, 0.08, 0.05, 0.06, 0.06, 0.21, 0.19, 0.28, 1.00, 0.15, 0.00, 0.25],
        [0.19, 0.23, 0.25, 0.20, 0.19, 0.14, 0.08, 0.07, 0.12, 0.06, 0.20, 0.10, 0.20, 0.15, 1.00, 0.00, 0.23],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00],
        [0.24, 0.56, 0.50, 0.53, 0.53, 0.25, 0.22, 0.14, 0.19, 0.11, 0.37, 0.23, 0.27, 0.25, 0.23, 0.00, 1.00],
    )
)

# p.24, 67: The group of high FX volatility currencies
high_vol_currency_group = ['ARS', 'BRL', 'MXN', 'TRY', 'ZAR']

# p.24, 69: Risk Weights for a currency depends on the group of the calculation currency
fx_rw = {
    "Regular": {
        "Regular": 7.3,
        "High":    13,
    },
    "High": {
        "Regular": 13,
        "High":    10.2,
    }
}

# p.24, 70: Historical Volatility Ratio for FX Risk Class
fx_hvr = 0.55

# p.24, 71: Vega Risk Weight for FX Risk Class
fx_vrw = 0.47

# p.24, 72: Correlations for FX
## Regular Vol FX Group
fx_reg_vol_corr = {
    "Regular": {
        "Regular": 0.50,
        "High":    0.28,
    },
    "High": {
        "Regular": 0.28,
        "High":    0.69,
    }
}

# p.25, 72: Correlations for FX Risk Factor
# High Vol FX Group
fx_high_vol_corr = {
    "Regular": {
        "Regular": 0.85,
        "High":    0.39,
    },
    "High": {
        "Regular": 0.39,
        "High":    0.50,
    }
}

# p.25, 73: Correlations for FX Volatility&Curvature Risk Factor
fx_vega_corr = 0.5 

# p.26, 74&75: Delta Concentration Thresholds for Interest Rate Risk
ir_delta_CT = {
    'Others' : 22,  # All other currencies
    'USD'    : 240, # Regular volatility, well-traded 
    'EUR'    : 240, # Regular volatility, well-traded 
    'GBP'    : 240, # Regular volatility, well-traded
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
    'JPY'    : 120, # Low volatility
}

# p.26, 76: Delta Concentration Thresholds for Credit Spread Risk Group
credit_delta_CT = {
    "Qualifying" : {
        1 : 0.49, # Sovereigns including central banks
        2 : 0.22, # Corporate entities 
        3 : 0.22, # Corporate entities
        4 : 0.22, # Corporate entities
        5 : 0.22, # Corporate entities
        6 : 0.22, # Corporate entities
        7 : 0.49, # Sovereigns including central banks
        8 : 0.22, # Corporate entities
        9 : 0.22, # Corporate entities
        10: 0.22, # Corporate entities
        11: 0.22, # Corporate entities
        12: 0.22, # Corporate entities
        0 : 0.22, # Residual
    }, 
    "Non-Qualifying" : {
        1 : 9.5, # Investment Grades(RMBS & CMBS) 
        2 : 0.5, # High Yield/Non-rated (RMBS & CMBS)
        0 : 0.5, # Residual
    }
}

# p.26, 77: Delta Concentration Thresholds for Equity Risk
equity_delta_CT = {
    1 : 9,    # Emerging Markets  - Large Cap
    2 : 9,    # Emerging Markets  - Large Cap
    3 : 9,    # Emerging Markets  - Large Cap
    4 : 9,    # Emerging Markets  - Large Cap
    5 : 18,   # Developed Markets - Large Cap
    6 : 18,   # Developed Markets - Large Cap
    7 : 18,   # Developed Markets - Large Cap
    8 : 18,   # Developed Markets - Large Cap
    9 : 1.2,  # Emerging Markets  - Small Cap
    10: 0.9,  # Developed Markets - Small Cap
    11: 1300, # Indexes, Funds, ETFs, Volatility Indexes
    12: 1300, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 0.9,  # Residual - Not classified
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
    11: 600,  # Base metals 
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
    'Category1' : 8300, # Significantly material 
    'Category2' : 1900, # Frequently traded 
    'Others'    : 240,  # All other currencies
}

# p.27, 81: Vega Concentration Thresholds for IR Risk
ir_vega_CT = {
    'Others' : 83,   # All other currencies
    'USD'    : 2600, # Regular volatility, well-traded 
    'EUR'    : 2600, # Regular volatility, well-traded 
    'GBP'    : 2600, # Regular volatility, well-traded
    'AUD'    : 270,  # Regular volatility, less well-traded 
    'CAD'    : 270,  # Regular volatility, less well-traded 
    'CHF'    : 270,  # Regular volatility, less well-traded 
    'DKK'    : 270,  # Regular volatility, less well-traded 
    'HKD'    : 270,  # Regular volatility, less well-traded 
    'KRW'    : 270,  # Regular volatility, less well-traded 
    'NOK'    : 270,  # Regular volatility, less well-traded 
    'NZD'    : 270,  # Regular volatility, less well-traded 
    'SEK'    : 270,  # Regular volatility, less well-traded 
    'SGD'    : 270,  # Regular volatility, less well-traded 
    'TWD'    : 270,  # Regular volatility, less well-traded
    'JPY'    : 980,  # Low volatility
}

# p.27, 83: Vega Concentration Thresholds for Credit Spread Risk
credit_vega_CT = {
    "Qualifying"     : 310, 
    "Non-Qualifying" : 85,
}

# p.28, 84: Vega Concentration Thresholds for Equity Risk
equity_vega_CT = {
    1 : 160,  # Emerging Markets  - Large Cap
    2 : 160,  # Emerging Markets  - Large Cap
    3 : 160,  # Emerging Markets  - Large Cap
    4 : 160,  # Emerging Markets  - Large Cap
    5 : 1600, # Developed Markets - Large Cap
    6 : 1600, # Developed Markets - Large Cap
    7 : 1600, # Developed Markets - Large Cap
    8 : 1600, # Developed Markets - Large Cap
    9 : 38,   # Emerging Markets  - Small Cap
    10: 260,  # Developed Markets - Small Cap
    11: 7000, # Indexes, Funds, ETFs, Volatility Indexes
    12: 7000, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 38,   # Residual - Not classified
}

# p.28, 85: Vega Concentration Thresholds for Commodity Risk
commodity_vega_CT = {
    1 : 160,  # Coal
    2 : 2600, # Crude Oil
    3 : 280,  # Oil Fractions 
    4 : 280,  # Oil Fractions 
    5 : 280,  # Oil Fractions 
    6 : 3500, # Natural Gas 
    7 : 3500, # Natural Gas 
    8 : 750,  # Power 
    9 : 750,  # Power 
    10: 89,   # Freight, Dry or Wet 
    11: 340,  # Base metals 
    12: 720,  # Precious Metals 
    13: 500,  # Agricultural 
    14: 500,  # Agricultural 
    15: 500,  # Agricultural 
    16: 63,   # Other 
    17: 63,  # Indices 
}

# p.28, 86: Vega Concentration Thresholds for FX Risk
fx_vega_CT = {
    'Category1-Category1' : 3000,
    'Category1-Category2' : 1400,
    'Category1-Category3' : 610,
    'Category2-Category2' : 640,
    'Category2-Category3' : 420,
    'Category3-Category3' : 240,
}

# p.29, 88: Correlation between Risk Classes within Product Classes
corr_params = list(
    zip(
        [1.00, 0.32, 0.19, 0.33, 0.41, 0.28],
        [0.32, 1.00, 0.45, 0.69, 0.52, 0.42],
        [0.19, 0.45, 1.00, 0.48, 0.40, 0.14],
        [0.33, 0.69, 0.48, 1.00, 0.52, 0.34],
        [0.41, 0.52, 0.40, 0.52, 1.00, 0.38],
        [0.28, 0.42, 0.14, 0.34, 0.38, 1.00],
    )
)