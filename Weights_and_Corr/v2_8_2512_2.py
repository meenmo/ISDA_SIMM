# The parameters below can be found at https://www.isda.org/a/hhkiE/ISDA-SIMM_v2.82512_PUBLIC.pdf

# p.14, 33
## Regular/Low Vol Currency Buckets
reg_vol_ccy_bucket = ['USD', 'EUR', 'GBP', 'CHF', 'AUD', 'NZD', 'CAD', 'SEK', 'NOK', 'DKK', 'HKD', 'KRW', 'SGD', 'TWD']
low_vol_ccy_bucket = ['JPY']

## table1: Risk Weights for Regular/Low/High Vol Currency Bucket Respectively
reg_vol_rw = {
    '2w'  : 107,
    '1m'  : 101,
    '3m'  : 90,
    '6m'  : 69,
    '1y'  : 68,
    '2y'  : 69,
    '3y'  : 66,
    '5y'  : 61,
    '10y' : 60,
    '15y' : 58,
    '20y' : 58,
    '30y' : 66,
}

low_vol_rw = {
    '2w'  : 15,
    '1m'  : 18,
    '3m'  : 12,
    '6m'  : 11,
    '1y'  : 15,
    '2y'  : 21,
    '3y'  : 23,
    '5y'  : 25,
    '10y' : 29,
    '15y' : 27,
    '20y' : 26,
    '30y' : 28,
}

high_vol_rw = {
    '2w'  : 167,
    '1m'  : 102,
    '3m'  : 79,
    '6m'  : 82,
    '1y'  : 90,
    '2y'  : 93,
    '3y'  : 92,
    '5y'  : 88,
    '10y' : 88,
    '15y' : 98,
    '20y' : 101,
    '30y' : 96,
}

## Risk Weights for Any Currency's Inflation Rate/Cross-Currency Basis Swap Spread
inflation_rw = 51
ccy_basis_swap_spread_rw = 21

# p.14, 34: The Historical Volatility Ratio for the Interest Rate Risk Class
ir_hvr = 0.74

# p.14, 35: The Vega Risk Weight for the Interest Rate Risk Class
ir_vrw = 0.20

# p.15, 36: IR - Correlations
## Correlations for Aggregated Weighted Sensitivities/Risk Exposures
ir_corr = list(
    zip(
        [1.00, 0.74, 0.65, 0.54, 0.40, 0.29, 0.25, 0.22, 0.17, 0.16, 0.14, 0.14],
        [0.74, 1.00, 0.85, 0.72, 0.50, 0.36, 0.30, 0.25, 0.20, 0.16, 0.14, 0.14],
        [0.65, 0.85, 1.00, 0.90, 0.69, 0.53, 0.46, 0.40, 0.34, 0.27, 0.25, 0.25],
        [0.54, 0.72, 0.90, 1.00, 0.86, 0.73, 0.65, 0.58, 0.52, 0.47, 0.44, 0.42],
        [0.40, 0.50, 0.69, 0.86, 1.00, 0.94, 0.87, 0.81, 0.73, 0.69, 0.64, 0.63],
        [0.29, 0.36, 0.53, 0.73, 0.94, 1.00, 0.97, 0.92, 0.86, 0.82, 0.77, 0.76],
        [0.25, 0.30, 0.46, 0.65, 0.87, 0.97, 1.00, 0.97, 0.91, 0.87, 0.82, 0.81],
        [0.22, 0.25, 0.40, 0.58, 0.81, 0.92, 0.97, 1.00, 0.96, 0.93, 0.89, 0.88],
        [0.17, 0.20, 0.34, 0.52, 0.73, 0.86, 0.91, 0.96, 1.00, 0.98, 0.95, 0.95],
        [0.16, 0.16, 0.27, 0.47, 0.69, 0.82, 0.87, 0.93, 0.98, 1.00, 0.98, 0.97],
        [0.14, 0.14, 0.25, 0.44, 0.64, 0.77, 0.82, 0.89, 0.95, 0.98, 1.00, 0.98],
        [0.14, 0.14, 0.25, 0.42, 0.63, 0.76, 0.81, 0.88, 0.95, 0.97, 0.98, 1.00],
    )
)
## The Correlation between any two sub-curves of the same currency
sub_curves_corr = 0.981
inflation_corr  = 0.42
ccy_basis_spread_corr = -0.01

# p.15, 37: The parameter for aggregating across different currencies
ir_gamma_diff_ccy = 0.35

# p.16, 39: Risk Weights for Credit Qualifying
creditQ_rw = {
    1:  68,
    2:  75,
    3:  75,
    4:  49,
    5:  53,
    6:  44,
    7:  165,
    8:  271,
    9:  136,
    10: 227,
    11: 423,
    12: 200,
    0:  423, # Residual
}

# p.17, 40: Vega Risk Weight for Credit Qualifying
creditQ_vrw = 0.42

# p.17, 41: Base Correlation Weight
base_corr_weight = 9.7

# p.17, 42: Credit Qualifying Correlations
# aggregate sensitivities for same issuer, aggregate sensitivities for different issuer, residual bucket, Base corr across different index families
creditQ_corr = [0.92,0.46,0.5,0.10]

# p.17, 43: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
creditQ_corr_non_res = list(
    zip(
        [1.00, 0.38, 0.38, 0.36, 0.36, 0.36, 0.41, 0.28, 0.34, 0.35, 0.35, 0.35],
        [0.38, 1.00, 0.45, 0.43, 0.42, 0.43, 0.42, 0.31, 0.39, 0.39, 0.38, 0.37],
        [0.38, 0.45, 1.00, 0.48, 0.47, 0.49, 0.43, 0.30, 0.42, 0.42, 0.41, 0.40],
        [0.36, 0.43, 0.48, 1.00, 0.46, 0.50, 0.42, 0.29, 0.39, 0.41, 0.39, 0.40],
        [0.36, 0.42, 0.47, 0.46, 1.00, 0.47, 0.40, 0.28, 0.38, 0.39, 0.39, 0.38],
        [0.36, 0.43, 0.49, 0.50, 0.47, 1.00, 0.42, 0.28, 0.39, 0.41, 0.39, 0.42],
        [0.41, 0.42, 0.43, 0.42, 0.40, 0.42, 1.00, 0.29, 0.37, 0.39, 0.36, 0.36],
        [0.28, 0.31, 0.30, 0.29, 0.28, 0.28, 0.29, 1.00, 0.28, 0.28, 0.27, 0.29],
        [0.34, 0.39, 0.42, 0.39, 0.38, 0.39, 0.37, 0.28, 1.00, 0.36, 0.36, 0.35],
        [0.35, 0.39, 0.42, 0.41, 0.39, 0.41, 0.39, 0.28, 0.36, 1.00, 0.36, 0.39],
        [0.35, 0.38, 0.41, 0.39, 0.39, 0.39, 0.36, 0.27, 0.36, 0.36, 1.00, 0.35],
        [0.35, 0.37, 0.40, 0.40, 0.38, 0.42, 0.36, 0.29, 0.35, 0.39, 0.35, 1.00],
    )
)
# p.18, 46: Risk Weights for Credit Non-Qualifying
creiditNonQ_rw = {
    1: 210,
    2: 2700,
    0: 2700, # Residual
}

# p.18, 47: Vega Risk Weight for Credit Non-Qualifying
creditNonQ_vrw = 0.42

# p.18, 48: Credit Non-Qualifying Correlations
creditNonQ_corr = [0.86,0.50,0.5]

# p.18, 49: Correlation between non-residual bucket
cr_gamma_diff_ccy = 0.79

# p.20, 56: Risk Weights for Equity Risk Class
equity_rw = {
    1:  29,
    2:  31,
    3:  31,
    4:  29,
    5:  23,
    6:  24,
    7:  27,
    8:  29,
    9:  34,
    10: 38,
    11: 15,
    12: 15,
    0:  38, # Residual
}

# p.20, 57: Historical Volatility Ratio for Equity Risk Class
equity_hvr = 0.56

# p.20, 58: Vega Risk Weight for Equity Risk Class
equity_vrw = 0.29
equity_vrw_bucket_12 = 0.72

# p.20, 59: Correlations for Equity Risk Class
equity_corr = {
    1:  0.14,
    2:  0.17,
    3:  0.24,
    4:  0.19,
    5:  0.18,
    6:  0.27,
    7:  0.30,
    8:  0.30,
    9:  0.22,
    10: 0.20,
    11: 0.39,
    12: 0.39,
    0:  0,   # Residual
}

# p.20, 60: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
equity_corr_non_res = list(
    zip(
        [1.00, 0.15, 0.17, 0.15, 0.11, 0.13, 0.13, 0.13, 0.16, 0.09, 0.15, 0.15],
        [0.15, 1.00, 0.19, 0.17, 0.11, 0.14, 0.15, 0.14, 0.18, 0.10, 0.16, 0.16],
        [0.17, 0.19, 1.00, 0.19, 0.12, 0.16, 0.20, 0.16, 0.20, 0.12, 0.18, 0.18],
        [0.15, 0.17, 0.19, 1.00, 0.14, 0.18, 0.19, 0.19, 0.18, 0.14, 0.22, 0.22],
        [0.11, 0.11, 0.12, 0.14, 1.00, 0.21, 0.20, 0.22, 0.10, 0.16, 0.24, 0.24],
        [0.13, 0.14, 0.16, 0.18, 0.21, 1.00, 0.26, 0.28, 0.14, 0.20, 0.30, 0.30],
        [0.13, 0.15, 0.20, 0.19, 0.20, 0.26, 1.00, 0.27, 0.15, 0.20, 0.30, 0.30],
        [0.13, 0.14, 0.16, 0.19, 0.22, 0.28, 0.27, 1.00, 0.13, 0.20, 0.32, 0.32],
        [0.16, 0.18, 0.20, 0.18, 0.10, 0.14, 0.15, 0.13, 1.00, 0.10, 0.15, 0.15],
        [0.09, 0.10, 0.12, 0.14, 0.16, 0.20, 0.20, 0.20, 0.10, 1.00, 0.20, 0.20],
        [0.15, 0.16, 0.18, 0.22, 0.24, 0.30, 0.30, 0.32, 0.15, 0.20, 1.00, 0.39],
        [0.15, 0.16, 0.18, 0.22, 0.24, 0.30, 0.30, 0.32, 0.15, 0.20, 0.39, 1.00],
    )
)

# p.22, 61: Risk Weights for Commodity Risk Class
commodity_rw = {
    1:  22,
    2:  21,
    3:  23,
    4:  18,
    5:  24,
    6:  22,
    7:  27,
    8:  36,
    9:  29,
    10: 44,
    11: 20,
    12: 19,
    13: 14,
    14: 17,
    15: 11,
    16: 44,
    17: 16,
}

# p.22, 62: Historical Volatility Ratio for Commodity Risk Class
commodity_hvr = 0.81

# p.22, 63: Vega Risk Weight for Commodity Risk Class
commodity_vrw = 0.34

# p.22, 64: Correlations for Commodity Risk Class
commodity_corr = {
    1:  0.72,
    2:  0.97,
    3:  0.98,
    4:  0.98,
    5:  0.98,
    6:  0.92,
    7:  0.92,
    8:  0.37,
    9:  0.65,
    10: 0.47,
    11: 0.61,
    12: 0.66,
    13: 0.61,
    14: 0.18,
    15: 0.17,
    16: 0.00,
    17: 0.31,
}

# p.23, 65: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
commodity_corr_non_res = list(
    zip(
        [1.00, 0.25, 0.20, 0.28, 0.27, 0.22, 0.56, 0.14, 0.36, 0.18, 0.14, 0.14, 0.24, 0.11, 0.04, 0.00, 0.23],
        [0.25, 1.00, 0.94, 0.92, 0.90, 0.21, 0.26, 0.12, 0.19, 0.17, 0.41, 0.27, 0.30, 0.25, 0.16, 0.00, 0.60],
        [0.20, 0.94, 1.00, 0.91, 0.88, 0.19, 0.26, 0.10, 0.13, 0.20, 0.41, 0.25, 0.30, 0.26, 0.12, 0.00, 0.59],
        [0.28, 0.92, 0.91, 1.00, 0.84, 0.28, 0.29, 0.18, 0.18, 0.19, 0.40, 0.23, 0.33, 0.22, 0.11, 0.00, 0.60],
        [0.27, 0.90, 0.88, 0.84, 1.00, 0.14, 0.30, 0.09, 0.19, 0.22, 0.40, 0.27, 0.30, 0.29, 0.15, 0.00, 0.56],
        [0.22, 0.21, 0.19, 0.28, 0.14, 1.00, 0.29, 0.55, 0.12, 0.08, 0.21, 0.10, 0.17, 0.02, 0.07, 0.00, 0.27],
        [0.56, 0.26, 0.26, 0.29, 0.30, 0.29, 1.00, 0.14, 0.55, 0.08, 0.14, 0.17, 0.29, 0.11, 0.07, 0.00, 0.29],
        [0.14, 0.12, 0.10, 0.18, 0.09, 0.55, 0.14, 1.00, 0.16, 0.01, 0.12, 0.07, 0.10, 0.03, 0.01, 0.00, 0.18],
        [0.36, 0.19, 0.13, 0.18, 0.19, 0.12, 0.55, 0.16, 1.00, 0.01, 0.14, 0.10, 0.21, 0.06, 0.06, 0.00, 0.17],
        [0.18, 0.17, 0.20, 0.19, 0.22, 0.08, 0.08, 0.01, 0.01, 1.00, 0.15, 0.13, 0.09, 0.09, 0.00, 0.00, 0.13],
        [0.14, 0.41, 0.41, 0.40, 0.40, 0.21, 0.14, 0.12, 0.14, 0.15, 1.00, 0.37, 0.27, 0.21, 0.16, 0.00, 0.40],
        [0.14, 0.27, 0.25, 0.23, 0.27, 0.10, 0.17, 0.07, 0.10, 0.13, 0.37, 1.00, 0.20, 0.18, 0.11, 0.00, 0.24],
        [0.24, 0.30, 0.30, 0.33, 0.30, 0.17, 0.29, 0.10, 0.21, 0.09, 0.27, 0.20, 1.00, 0.16, 0.10, 0.00, 0.31],
        [0.11, 0.25, 0.26, 0.22, 0.29, 0.02, 0.11, 0.03, 0.06, 0.09, 0.21, 0.18, 0.16, 1.00, 0.14, 0.00, 0.20],
        [0.04, 0.16, 0.12, 0.11, 0.15, 0.07, 0.07, 0.01, 0.06, 0.00, 0.16, 0.11, 0.10, 0.14, 1.00, 0.00, 0.17],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00],
        [0.23, 0.60, 0.59, 0.60, 0.56, 0.27, 0.29, 0.18, 0.17, 0.13, 0.40, 0.24, 0.31, 0.20, 0.17, 0.00, 1.00],
    )
)

# p.24, 67: The group of high FX volatility currencies
high_vol_currency_group = ['ARS', 'EGP', 'ETB', 'GHS', 'ISK', 'LBP', 'NGN', 'SCR', 'ZMW']

# p.24, 69: Risk Weights for a currency depends on the group of the calculation currency
fx_rw = {
    "Regular": {
        "Regular": 7.4,
        "High":    31.7,
    },
    "High": {
        "Regular": 31.7,
        "High":    31.7,
    }
}

# p.24, 70: Historical Volatility Ratio for FX Risk Class
fx_hvr = 0.67

# p.24, 71: Vega Risk Weight for FX Risk Class
fx_vrw = 0.33

# p.24, 72: Correlations for FX
## Regular Vol FX Group
fx_reg_vol_corr = {
    "Regular": {
        "Regular": 0.50,
        "High":    0.12,
    },
    "High": {
        "Regular": 0.12,
        "High":    0.03,
    }
}

# p.25, 72: Correlations for FX Risk Factor
# High Vol FX Group
fx_high_vol_corr = {
    "Regular": {
        "Regular": 0.97,
        "High":    0.70,
    },
    "High": {
        "Regular": 0.70,
        "High":    0.50,
    }
}

# p.25, 73: Correlations for FX Volatility&Curvature Risk Factor
fx_vega_corr = 0.5

# p.26, 74&75: Delta Concentration Thresholds for Interest Rate Risk
ir_delta_CT = {
    'Others' : 71,   # All other currencies
    'USD'    : 220,  # Regular volatility, well-traded
    'EUR'    : 220,  # Regular volatility, well-traded
    'GBP'    : 220,  # Regular volatility, well-traded
    'AUD'    : 110,  # Regular volatility, less well-traded
    'CAD'    : 110,  # Regular volatility, less well-traded
    'CHF'    : 110,  # Regular volatility, less well-traded
    'DKK'    : 110,  # Regular volatility, less well-traded
    'HKD'    : 110,  # Regular volatility, less well-traded
    'KRW'    : 110,  # Regular volatility, less well-traded
    'NOK'    : 110,  # Regular volatility, less well-traded
    'NZD'    : 110,  # Regular volatility, less well-traded
    'SEK'    : 110,  # Regular volatility, less well-traded
    'SGD'    : 110,  # Regular volatility, less well-traded
    'TWD'    : 110,  # Regular volatility, less well-traded
    'JPY'    : 370,  # Low volatility
}

# p.26, 76: Delta Concentration Thresholds for Credit Spread Risk Group
credit_delta_CT = {
    "Qualifying" : {
        1 : 1,    # Sovereigns including central banks
        2 : 0.19, # Corporate entities
        3 : 0.19, # Corporate entities
        4 : 0.19, # Corporate entities
        5 : 0.19, # Corporate entities
        6 : 0.19, # Corporate entities
        7 : 1,    # Sovereigns including central banks
        8 : 0.19, # Corporate entities
        9 : 0.19, # Corporate entities
        10: 0.19, # Corporate entities
        11: 0.19, # Corporate entities
        12: 0.19, # Corporate entities
        0 : 0.19, # Residual
    },
    "Non-Qualifying" : {
        1 : 0.19, # Investment Grades(RMBS & CMBS)
        2 : 0.19, # High Yield/Non-rated (RMBS & CMBS)
        0 : 0.19, # Residual
    }
}

# p.26, 77: Delta Concentration Thresholds for Equity Risk
equity_delta_CT = {
    1 : 4,     # Emerging Markets  - Large Cap
    2 : 4,     # Emerging Markets  - Large Cap
    3 : 4,     # Emerging Markets  - Large Cap
    4 : 4,     # Emerging Markets  - Large Cap
    5 : 20,    # Developed Markets - Large Cap
    6 : 20,    # Developed Markets - Large Cap
    7 : 20,    # Developed Markets - Large Cap
    8 : 20,    # Developed Markets - Large Cap
    9 : 0.98,  # Emerging Markets  - Small Cap
    10: 0.4,   # Developed Markets - Small Cap
    11: 650,   # Indexes, Funds, ETFs, Volatility Indexes
    12: 650,   # Indexes, Funds, ETFs, Volatility Indexes
    0 : 0.4,   # Residual - Not classified
}

# p.27, 78: Delta Concentration Thresholds for Commodity Risk
commodity_delta_CT = {
    1 : 310,  # Coal
    2 : 2500, # Crude Oil
    3 : 1700, # Oil Fractions
    4 : 1700, # Oil Fractions
    5 : 1700, # Oil Fractions
    6 : 2300, # Natural Gas
    7 : 2300, # Natural Gas
    8 : 1600, # Power
    9 : 1600, # Power
    10: 52,   # Freight, Dry or Wet
    11: 570,  # Base metals
    12: 1600, # Precious Metals
    13: 100,  # Agricultural
    14: 100,  # Agricultural
    15: 100,  # Agricultural
    16: 52,   # Other
    17: 4000, # Indices
}

# p.27, 80: Currency Categories
fx_category1 = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CHF', 'CAD'] # Significantly material
fx_category2 = ['BRL', 'CNY', 'HKD', 'INR', 'KRW', 'MXN', 'NOK', 'NZD', 'RUB', 'SEK', 'SGD', 'TRY', 'ZAR'] # Frequently traded

# p.27, 79: Delta Concentration Thresholds for FX Risk
fx_delta_CT = {
    'Category1' : 2100, # Significantly material
    'Category2' : 710,  # Frequently traded
    'Others'    : 120,  # All other currencies
}

# p.27, 81: Vega Concentration Thresholds for IR Risk
ir_vega_CT = {
    'Others' : 160,  # All other currencies
    'USD'    : 3800, # Regular volatility, well-traded
    'EUR'    : 3800, # Regular volatility, well-traded
    'GBP'    : 3800, # Regular volatility, well-traded
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
    'JPY'    : 1100, # Low volatility
}

# p.27, 83: Vega Concentration Thresholds for Credit Spread Risk
credit_vega_CT = {
    "Qualifying"     : 300,
    "Non-Qualifying" : 2.1,
}

# p.28, 84: Vega Concentration Thresholds for Equity Risk
equity_vega_CT = {
    1 : 370,  # Emerging Markets  - Large Cap
    2 : 370,  # Emerging Markets  - Large Cap
    3 : 370,  # Emerging Markets  - Large Cap
    4 : 370,  # Emerging Markets  - Large Cap
    5 : 1100, # Developed Markets - Large Cap
    6 : 1100, # Developed Markets - Large Cap
    7 : 1100, # Developed Markets - Large Cap
    8 : 1100, # Developed Markets - Large Cap
    9 : 100,  # Emerging Markets  - Small Cap
    10: 260,  # Developed Markets - Small Cap
    11: 3800, # Indexes, Funds, ETFs, Volatility Indexes
    12: 3800, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 100,  # Residual - Not classified
}

# p.28, 85: Vega Concentration Thresholds for Commodity Risk
commodity_vega_CT = {
    1 : 200,  # Coal
    2 : 2200, # Crude Oil
    3 : 230,  # Oil Fractions
    4 : 230,  # Oil Fractions
    5 : 230,  # Oil Fractions
    6 : 3300, # Natural Gas
    7 : 3300, # Natural Gas
    8 : 730,  # Power
    9 : 730,  # Power
    10: 89,   # Freight, Dry or Wet
    11: 450,  # Base metals
    12: 770,  # Precious Metals
    13: 630,  # Agricultural
    14: 630,  # Agricultural
    15: 630,  # Agricultural
    16: 56,   # Other
    17: 56,   # Indices
}

# p.28, 86: Vega Concentration Thresholds for FX Risk
fx_vega_CT = {
    'Category1-Category1' : 2900,
    'Category1-Category2' : 1500,
    'Category1-Category3' : 840,
    'Category2-Category2' : 760,
    'Category2-Category3' : 490,
    'Category3-Category3' : 310,
}

# p.29, 88: Correlation between Risk Classes within Product Classes
corr_params = list(
    zip(
        [1.00, 0.09, 0.07, 0.11, 0.34, 0.15],
        [0.09, 1.00, 0.62, 0.61, 0.35, 0.25],
        [0.07, 0.62, 1.00, 0.47, 0.28, 0.14],
        [0.11, 0.61, 0.47, 1.00, 0.41, 0.25],
        [0.34, 0.35, 0.28, 0.41, 1.00, 0.28],
        [0.15, 0.25, 0.14, 0.25, 0.28, 1.00],
    )
)
