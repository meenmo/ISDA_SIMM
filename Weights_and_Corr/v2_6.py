# The parameters below can be found at https://www.isda.org/a/b4ugE/ISDA-SIMM_v2.6_PUBLIC.pdf

# p.14, 33
## Regular/Low Vol Currency Buckets
reg_vol_ccy_bucket = ['USD', 'EUR', 'GBP', 'CHF', 'AUD', 'NZD', 'CAD', 'SEK', 'NOK', 'DKK', 'HKD', 'KRW', 'SGD', 'TWD']
low_vol_ccy_bucket = ['JPY']

## table1: Risk Weights for Regular/Low/High Vol Currency Bucket Respectively
reg_vol_rw = {
    '2w'  : 109,
    '1m'  : 105,
    '3m'  : 90,
    '6m'  : 71,
    '1y'  : 66,
    '2y'  : 66,
    '3y'  : 64,
    '5y'  : 60,
    '10y' : 60,
    '15y' : 61,
    '20y' : 61,
    '30y' : 67,
}

low_vol_rw = {
    '2w'  : 15, 
    '1m'  : 18, 
    '3m'  : 9,
    '6m'  : 11,
    '1y'  : 13,
    '2y'  : 15,
    '3y'  : 19,
    '5y'  : 23,
    '10y' : 23,
    '15y' : 22,
    '20y' : 22,
    '30y' : 23,
}

high_vol_rw = {
    '2w'  : 163, 
    '1m'  : 109, 
    '3m'  : 87,
    '6m'  : 89,
    '1y'  : 102,
    '2y'  : 96,
    '3y'  : 101,
    '5y'  : 97,
    '10y' : 97,
    '15y' : 102,
    '20y' : 106,
    '30y' : 101,
}

## Risk Weights for Any Currency's Inflation Rate/Cross-Currency Basis Swap Spread
inflation_rw = 61
ccy_basis_swap_spread_rw = 21

# p.14, 34: The Historical Volatility Ratio for the Interest Rate Risk Class
ir_hvr = 0.47

# p.14, 35: The Vega Risk Weight for the Interest Rate Risk Class
ir_vrw = 0.23

# p.15, 36: IR - Correlations
## Correlations for Aggregated Weighted Sensitivities/Risk Exposures
ir_corr = list(
    zip(
        [1.00, 0.77, 0.67, 0.59, 0.48, 0.39, 0.34, 0.30, 0.25, 0.23, 0.21, 0.20],
        [0.77, 1.00, 0.84, 0.74, 0.56, 0.43, 0.36, 0.31, 0.26, 0.21, 0.19, 0.19],
        [0.67, 0.84, 1.00, 0.88, 0.69, 0.55, 0.47, 0.40, 0.34, 0.27, 0.25, 0.25],
        [0.59, 0.74, 0.88, 1.00, 0.86, 0.73, 0.65, 0.57, 0.49, 0.40, 0.38, 0.37],
        [0.48, 0.56, 0.69, 0.86, 1.00, 0.94, 0.87, 0.79, 0.68, 0.60, 0.57, 0.55],
        [0.39, 0.43, 0.55, 0.73, 0.94, 1.00, 0.96, 0.91, 0.80, 0.74, 0.70, 0.69],
        [0.34, 0.36, 0.47, 0.65, 0.87, 0.96, 1.00, 0.97, 0.88, 0.81, 0.77, 0.76],
        [0.30, 0.31, 0.40, 0.57, 0.79, 0.91, 0.97, 1.00, 0.95, 0.90, 0.86, 0.85],
        [0.25, 0.26, 0.34, 0.49, 0.68, 0.80, 0.88, 0.95, 1.00, 0.97, 0.94, 0.94],
        [0.23, 0.21, 0.27, 0.40, 0.60, 0.74, 0.81, 0.90, 0.97, 1.00, 0.98, 0.97],
        [0.21, 0.19, 0.25, 0.38, 0.57, 0.70, 0.77, 0.86, 0.94, 0.98, 1.00, 0.99],
        [0.20, 0.19, 0.25, 0.37, 0.55, 0.69, 0.76, 0.85, 0.94, 0.97, 0.99, 1.00],
    )
)
## The Correlation between any two sub-curves of the same currency
sub_curves_corr = 0.993
inflation_corr  = 0.24
ccy_basis_spread_corr = 0.04

# p.15, 37: The parameter for aggregating across different currencies
ir_gamma_diff_ccy = 0.32

# p.16, 39: Risk Weights for Credit Qualifying
creditQ_rw = {
    1:  75,
    2:  90,
    3:  84,
    4:  54,
    5:  62,
    6:  48,
    7:  185,
    8:  343,
    9:  255,
    10: 250,
    11: 214,
    12: 173,
    0:  343, # Residual
}

# p.17, 40: Vega Risk Weight for Credit Qualifying
creditQ_vrw = 0.76

# p.17, 41: Base Correlation Weight
base_corr_weight = 10

# p.17, 42: Credit Qualifying Correlations
creditQ_corr = [0.93,0.46,0.5,0.29]

# p.17, 43: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
creditQ_corr_non_res = list(
    zip(
        [1.00, 0.38, 0.38, 0.35, 0.37, 0.34, 0.42, 0.32, 0.34, 0.33, 0.34, 0.33],
        [0.38, 1.00, 0.48, 0.46, 0.48, 0.46, 0.39, 0.40, 0.41, 0.41, 0.43, 0.40],
        [0.38, 0.48, 1.00, 0.50, 0.51, 0.50, 0.40, 0.39, 0.45, 0.44, 0.47, 0.42],
        [0.35, 0.46, 0.50, 1.00, 0.50, 0.50, 0.37, 0.37, 0.41, 0.43, 0.45, 0.40],
        [0.37, 0.48, 0.51, 0.50, 1.00, 0.50, 0.39, 0.38, 0.43, 0.43, 0.46, 0.42],
        [0.34, 0.46, 0.50, 0.50, 0.50, 1.00, 0.37, 0.35, 0.39, 0.41, 0.44, 0.41],
        [0.42, 0.39, 0.40, 0.37, 0.39, 0.37, 1.00, 0.33, 0.37, 0.37, 0.35, 0.35],
        [0.32, 0.40, 0.39, 0.37, 0.38, 0.35, 0.33, 1.00, 0.36, 0.37, 0.37, 0.36],
        [0.34, 0.41, 0.45, 0.41, 0.43, 0.39, 0.37, 0.36, 1.00, 0.41, 0.40, 0.38],
        [0.33, 0.41, 0.44, 0.43, 0.43, 0.41, 0.37, 0.37, 0.41, 1.00, 0.41, 0.39],
        [0.34, 0.43, 0.47, 0.45, 0.46, 0.44, 0.35, 0.37, 0.40, 0.41, 1.00, 0.40],
        [0.33, 0.40, 0.42, 0.40, 0.42, 0.41, 0.35, 0.36, 0.38, 0.39, 0.40, 1.00],
    )
)
# p.18, 46: Risk Weights for Credit Non-Qualifying
creiditNonQ_rw = {
    1: 280,
    2: 1300,
    0: 1300, # Residual
}

# p.18, 47: Vega Risk Weight for Credit Non-Qualifying
creditNonQ_vrw = 0.76

# p.18, 48: Credit Non-Qualifying Correlations
creditNonQ_corr = [0.83,0.32,0.5]

# p.18, 49: Correlation between non-residual bucket
cr_gamma_diff_ccy = 0.43

# p.20, 56: Risk Weights for Equity Risk Class
equity_rw = {
    1:  30,
    2:  33,
    3:  36,
    4:  29,
    5:  26,
    6:  25,
    7:  34,
    8:  28,
    9:  36,
    10: 50,
    11: 19,
    12: 19,
    0:  50, # Residual
}

# p.20, 57: Historical Volatility Ratio for Equity Risk Class
equity_hvr = 0.60

# p.20, 58: Vega Risk Weight for Equity Risk Class 
equity_vrw = 0.45
equity_vrw_bucket_12 = 0.96

# p.20, 59: Correlations for Equity Risk Class
equity_corr = {
    1:  0.18,
    2:  0.20,
    3:  0.28,
    4:  0.24,
    5:  0.25,
    6:  0.36,
    7:  0.35,
    8:  0.37,
    9:  0.23,
    10: 0.27,
    11: 0.45,
    12: 0.45,
    0:  0,   # Residual
}

# p.20, 60: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
equity_corr_non_res = list(
    zip(
        [1.00, 0.18, 0.19, 0.19, 0.14, 0.16, 0.15, 0.16, 0.18, 0.12, 0.19, 0.19],
        [0.18, 1.00, 0.22, 0.21, 0.15, 0.18, 0.17, 0.19, 0.20, 0.14, 0.21, 0.21],
        [0.19, 0.22, 1.00, 0.22, 0.13, 0.16, 0.18, 0.17, 0.22, 0.13, 0.20, 0.20],
        [0.19, 0.21, 0.22, 1.00, 0.17, 0.22, 0.22, 0.23, 0.22, 0.17, 0.26, 0.26],
        [0.14, 0.15, 0.13, 0.17, 1.00, 0.29, 0.26, 0.29, 0.14, 0.24, 0.32, 0.32],
        [0.16, 0.18, 0.16, 0.22, 0.29, 1.00, 0.34, 0.36, 0.17, 0.30, 0.39, 0.39],
        [0.15, 0.17, 0.18, 0.22, 0.26, 0.34, 1.00, 0.33, 0.16, 0.28, 0.36, 0.36],
        [0.16, 0.19, 0.17, 0.23, 0.29, 0.36, 0.33, 1.00, 0.17, 0.29, 0.40, 0.40],
        [0.18, 0.20, 0.22, 0.22, 0.14, 0.17, 0.16, 0.17, 1.00, 0.13, 0.21, 0.21],
        [0.12, 0.14, 0.13, 0.17, 0.24, 0.30, 0.28, 0.29, 0.13, 1.00, 0.30, 0.30],
        [0.19, 0.21, 0.20, 0.26, 0.32, 0.39, 0.36, 0.40, 0.21, 0.30, 1.00, 0.45],
        [0.19, 0.21, 0.20, 0.26, 0.32, 0.39, 0.36, 0.40, 0.21, 0.30, 0.45, 1.00],
    )
)

# p.22, 61: Risk Weights for Commodity Risk Class
commodity_rw = {
    1:  48,
    2:  29,
    3:  33,
    4:  25,
    5:  35,
    6:  30,
    7:  60,
    8:  52,
    9:  68,
    10: 63,
    11: 21,
    12: 21,
    13: 15,
    14: 16,
    15: 13,
    16: 68,
    17: 17,
}

# p.22, 62: Historical Volatility Ratio for Commodity Risk Class
commodity_hvr = 0.74

# p.22, 63: Vega Risk Weight for Commodity Risk Class
commodity_vrw = 0.55

# p.22, 64: Correlations for Commodity Risk Class
commodity_corr = {
    1:  0.83,
    2:  0.97,
    3:  0.93,
    4:  0.97,
    5:  0.98,
    6:  0.90,
    7:  0.98,
    8:  0.49,
    9:  0.80,
    10: 0.46,
    11: 0.58,
    12: 0.53,
    13: 0.62,
    14: 0.16,
    15: 0.18,
    16: 0.00,
    17: 0.38,
}

# p.23, 65: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
commodity_corr_non_res = list(
    zip(
        [1.00, 0.22, 0.18, 0.21, 0.20, 0.24,  0.49,  0.16,  0.38, 0.14,	0.10,  0.02, 0.12, 0.11,  0.02,	0.00, 0.17],
        [0.22, 1.00, 0.92, 0.90, 0.88, 0.25,  0.08,  0.19,  0.17, 0.17,	0.42,  0.28, 0.36, 0.27,  0.20,	0.00, 0.64],
        [0.18, 0.92, 1.00, 0.87, 0.84, 0.16,  0.07,  0.15,  0.10, 0.18,	0.33,  0.22, 0.27, 0.23,  0.16,	0.00, 0.54],
        [0.21, 0.90, 0.87, 1.00, 0.77, 0.19,  0.11,  0.18,  0.16, 0.14,	0.32,  0.22, 0.28, 0.22,  0.11,	0.00, 0.58],
        [0.20, 0.88, 0.84, 0.77, 1.00, 0.19,  0.09,  0.12,  0.13, 0.18,	0.42,  0.34, 0.32, 0.29,  0.13,	0.00, 0.59],
        [0.24, 0.25, 0.16, 0.19, 0.19, 1.00,  0.31,  0.62,  0.23, 0.10,	0.21,  0.05, 0.18, 0.10,  0.08,	0.00, 0.28],
        [0.49, 0.08, 0.07, 0.11, 0.09, 0.31,  1.00,  0.21,  0.79, 0.17,	0.10, -0.08, 0.10, 0.07, -0.02,	0.00, 0.13],
        [0.16, 0.19, 0.15, 0.18, 0.12, 0.62,  0.21,  1.00,  0.16, 0.08,	0.13, -0.07, 0.07, 0.05,  0.02,	0.00, 0.19],
        [0.38, 0.17, 0.10, 0.16, 0.13, 0.23,  0.79,  0.16,  1.00, 0.15,	0.09, -0.06, 0.06, 0.06,  0.01,	0.00, 0.16],
        [0.14, 0.17, 0.18, 0.14, 0.18, 0.10,  0.17,  0.08,  0.15, 1.00,	0.16,  0.09, 0.14, 0.09,  0.03,	0.00, 0.11],
        [0.10, 0.42, 0.33, 0.32, 0.42, 0.21,  0.10,  0.13,  0.09, 0.16,	1.00,  0.36, 0.30, 0.25,  0.18,	0.00, 0.37],
        [0.02, 0.28, 0.22, 0.22, 0.34, 0.05, -0.08, -0.07, -0.06, 0.09,	0.36,  1.00, 0.20, 0.18,  0.11,	0.00, 0.26],
        [0.12, 0.36, 0.27, 0.28, 0.32, 0.18,  0.10,  0.07,  0.06, 0.14,	0.30,  0.20, 1.00, 0.28,  0.19,	0.00, 0.39],
        [0.11, 0.27, 0.23, 0.22, 0.29, 0.10,  0.07,  0.05,  0.06, 0.09,	0.25,  0.18, 0.28, 1.00,  0.13,	0.00, 0.26],
        [0.02, 0.20, 0.16, 0.11, 0.13, 0.08, -0.02,  0.02,  0.01, 0.03,	0.18,  0.11, 0.19, 0.13,  1.00,	0.00, 0.21],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00,  0.00,  0.00,  0.00, 0.00,	0.00,  0.00, 0.00, 0.00,  0.00,	1.00, 0.00],
        [0.17, 0.64, 0.54, 0.58, 0.59, 0.28,  0.13,  0.19,  0.16, 0.11,	0.37,  0.26, 0.39, 0.26,  0.21,	0.00, 1.00],
    )
)

# p.24, 67: The group of high FX volatility currencies
high_vol_currency_group = ['BRL', 'RUB', 'TRY']

# p.24, 69: Risk Weights for a currency depends on the group of the calculation currency
fx_rw = {
    "Regular": {
        "Regular": 7.4,
        "High":    14.7,
    },
    "High": {
        "Regular": 14.7,
        "High":    21.4,
    }
}

# p.24, 70: Historical Volatility Ratio for FX Risk Class
fx_hvr = 0.57

# p.24, 71: Vega Risk Weight for FX Risk Class
fx_vrw = 0.48

# p.24, 72: Correlations for FX
## Regular Vol FX Group
fx_reg_vol_corr = {
    "Regular": {
        "Regular": 0.50,
        "High":    0.25,
    },
    "High": {
        "Regular": 0.25,
        "High":   -0.05,
    }
}

# p.25, 72: Correlations for FX Risk Factor
# High Vol FX Group
fx_high_vol_corr = {
    "Regular": {
        "Regular": 0.88,
        "High":    0.72,
    },
    "High": {
        "Regular": 0.72,
        "High":    0.50,
    }
}

# p.25, 73: Correlations for FX Volatility&Curvature Risk Factor
fx_vega_corr = 0.5 

# p.26, 74&75: Delta Concentration Thresholds for Interest Rate Risk
ir_delta_CT = {
    'Others' : 30,   # All other currencies
    'USD'    : 330,  # Regular volatility, well-traded 
    'EUR'    : 330,  # Regular volatility, well-traded 
    'GBP'    : 330,  # Regular volatility, well-traded
    'AUD'    : 130,  # Regular volatility, less well-traded 
    'CAD'    : 130,  # Regular volatility, less well-traded 
    'CHF'    : 130,  # Regular volatility, less well-traded 
    'DKK'    : 130,  # Regular volatility, less well-traded 
    'HKD'    : 130,  # Regular volatility, less well-traded 
    'KRW'    : 130,  # Regular volatility, less well-traded 
    'NOK'    : 130,  # Regular volatility, less well-traded 
    'NZD'    : 130,  # Regular volatility, less well-traded 
    'SEK'    : 130,  # Regular volatility, less well-traded 
    'SGD'    : 130,  # Regular volatility, less well-traded 
    'TWD'    : 130,  # Regular volatility, less well-traded
    'JPY'    : 61,   # Low volatility
}

# p.26, 76: Delta Concentration Thresholds for Credit Spread Risk Group
credit_delta_CT = {
    "Qualifying" : {
        1 : 1.00, # Sovereigns including central banks
        2 : 0.17, # Corporate entities 
        3 : 0.17, # Corporate entities
        4 : 0.17, # Corporate entities
        5 : 0.17, # Corporate entities
        6 : 0.17, # Corporate entities
        7 : 1.00, # Sovereigns including central banks
        8 : 0.17, # Corporate entities
        9 : 0.17, # Corporate entities
        10: 0.17, # Corporate entities
        11: 0.17, # Corporate entities
        12: 0.17, # Corporate entities
        0 : 0.17, # Residual
    }, 
    "Non-Qualifying" : {
        1 : 9.5, # Investment Grades(RMBS & CMBS) 
        2 : 0.5, # High Yield/Non-rated (RMBS & CMBS)
        0 : 0.5, # Residual
    }
}

# p.26, 77: Delta Concentration Thresholds for Equity Risk
equity_delta_CT = {
    1 : 3,     # Emerging Markets  - Large Cap
    2 : 3,     # Emerging Markets  - Large Cap
    3 : 3,     # Emerging Markets  - Large Cap
    4 : 3,     # Emerging Markets  - Large Cap
    5 : 12,    # Developed Markets - Large Cap
    6 : 12,    # Developed Markets - Large Cap
    7 : 12,    # Developed Markets - Large Cap
    8 : 12,    # Developed Markets - Large Cap
    9 : 0.64,  # Emerging Markets  - Small Cap
    10: 0.37,  # Developed Markets - Small Cap
    11: 810,   # Indexes, Funds, ETFs, Volatility Indexes
    12: 810,   # Indexes, Funds, ETFs, Volatility Indexes
    0 : 0.37,  # Residual - Not classified
}

# p.27, 78: Delta Concentration Thresholds for Commodity Risk
commodity_delta_CT = {
    1 : 310,  # Coal
    2 : 2100, # Crude Oil
    3 : 1700, # Oil Fractions 
    4 : 1700, # Oil Fractions 
    5 : 1700, # Oil Fractions 
    6 : 2800, # Natural Gas 
    7 : 2800, # Natural Gas 
    8 : 2700, # Power 
    9 : 2700, # Power 
    10: 52,   # Freight, Dry or Wet 
    11: 530,  # Base metals 
    12: 1300, # Precious Metals 
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
    'Category1' : 3300, # Significantly material 
    'Category2' : 880,  # Frequently traded 
    'Others'    : 170,  # All other currencies
}

# p.27, 81: Vega Concentration Thresholds for IR Risk
ir_vega_CT = {
    'Others' : 74,   # All other currencies
    'USD'    : 4900, # Regular volatility, well-traded 
    'EUR'    : 4900, # Regular volatility, well-traded 
    'GBP'    : 4900, # Regular volatility, well-traded
    'AUD'    : 520,  # Regular volatility, less well-traded 
    'CAD'    : 520,  # Regular volatility, less well-traded 
    'CHF'    : 520,  # Regular volatility, less well-traded 
    'DKK'    : 520,  # Regular volatility, less well-traded 
    'HKD'    : 520,  # Regular volatility, less well-traded 
    'KRW'    : 520,  # Regular volatility, less well-traded 
    'NOK'    : 520,  # Regular volatility, less well-traded 
    'NZD'    : 520,  # Regular volatility, less well-traded 
    'SEK'    : 520,  # Regular volatility, less well-traded 
    'SGD'    : 520,  # Regular volatility, less well-traded 
    'TWD'    : 520,  # Regular volatility, less well-traded
    'JPY'    : 970,  # Low volatility
}

# p.27, 83: Vega Concentration Thresholds for Credit Spread Risk
credit_vega_CT = {
    "Qualifying"     : 360, 
    "Non-Qualifying" : 70,
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
    9 : 39,   # Emerging Markets  - Small Cap
    10: 190,  # Developed Markets - Small Cap
    11: 6400, # Indexes, Funds, ETFs, Volatility Indexes
    12: 6400, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 39,   # Residual - Not classified
}

# p.28, 85: Vega Concentration Thresholds for Commodity Risk
commodity_vega_CT = {
    1 : 390,  # Coal
    2 : 2900, # Crude Oil
    3 : 310,  # Oil Fractions 
    4 : 310,  # Oil Fractions 
    5 : 310,  # Oil Fractions 
    6 : 6300, # Natural Gas 
    7 : 6300, # Natural Gas 
    8 : 1200,  # Power 
    9 : 1200,  # Power 
    10: 120,  # Freight, Dry or Wet 
    11: 390,  # Base metals 
    12: 1300,  # Precious Metals 
    13: 590,  # Agricultural 
    14: 590,  # Agricultural 
    15: 590,  # Agricultural 
    16: 69,   # Other 
    17: 69,   # Indices 
}

# p.28, 86: Vega Concentration Thresholds for FX Risk
fx_vega_CT = {
    'Category1-Category1' : 2800,
    'Category1-Category2' : 1400,
    'Category1-Category3' : 590,
    'Category2-Category2' : 520,
    'Category2-Category3' : 340,
    'Category3-Category3' : 210,
}

# p.29, 88: Correlation between Risk Classes within Product Classes
corr_params = list(
    zip(
        [1.00, 0.04, 0.04, 0.07, 0.37, 0.14],
        [0.04, 1.00, 0.54, 0.70, 0.27, 0.37],
        [0.04, 0.54, 1.00, 0.46, 0.24, 0.15],
        [0.07, 0.70, 0.46, 1.00, 0.35, 0.39],
        [0.37, 0.27, 0.24, 0.35, 1.00, 0.35],
        [0.14, 0.37, 0.15, 0.39, 0.35, 1.00],
    )
)