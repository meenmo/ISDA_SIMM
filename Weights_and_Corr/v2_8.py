# The parameters below can be found at https://www.isda.org/a/f2RgE/ISDA-SIMM_v2.82506_PUBLIC.pdf

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
    1:  67,
    2:  78,
    3:  78,
    4:  49,
    5:  56,
    6:  46,
    7:  172,
    8:  327,
    9:  159,
    10: 227,
    11: 326,
    12: 200,
    0:  327, # Residual
}

# p.17, 40: Vega Risk Weight for Credit Qualifying
creditQ_vrw = 0.42

# p.17, 41: Base Correlation Weight
base_corr_weight = 9.6

# p.17, 42: Credit Qualifying Correlations
# aggregate sensitivities for same issuer, aggregate sensitivities for different issuer, residual bucket, Base corr across different index families
creditQ_corr = [0.93,0.47,0.5,0.13]

# p.17, 43: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
creditQ_corr_non_res = list(
    zip(
        [1.00, 0.40, 0.39, 0.37, 0.38, 0.36, 0.43, 0.29, 0.36, 0.35, 0.35, 0.35],
        [0.40, 1.00, 0.46, 0.44, 0.44, 0.44, 0.41, 0.30, 0.41, 0.40, 0.40, 0.36],
        [0.39, 0.46, 1.00, 0.49, 0.48, 0.50, 0.42, 0.28, 0.44, 0.43, 0.43, 0.39],
        [0.37, 0.44, 0.49, 1.00, 0.47, 0.50, 0.40, 0.27, 0.42, 0.42, 0.41, 0.38],
        [0.38, 0.44, 0.48, 0.47, 1.00, 0.48, 0.39, 0.27, 0.41, 0.40, 0.41, 0.37],
        [0.36, 0.44, 0.50, 0.50, 0.48, 1.00, 0.41, 0.26, 0.41, 0.41, 0.42, 0.42],
        [0.43, 0.41, 0.42, 0.40, 0.39, 0.41, 1.00, 0.28, 0.39, 0.38, 0.38, 0.35],
        [0.29, 0.30, 0.28, 0.27, 0.27, 0.26, 0.28, 1.00, 0.27, 0.27, 0.26, 0.25],
        [0.36, 0.41, 0.44, 0.42, 0.41, 0.41, 0.39, 0.27, 1.00, 0.39, 0.38, 0.35],
        [0.35, 0.40, 0.43, 0.42, 0.40, 0.41, 0.38, 0.27, 0.39, 1.00, 0.38, 0.37],
        [0.35, 0.40, 0.43, 0.41, 0.41, 0.42, 0.38, 0.26, 0.38, 0.38, 1.00, 0.35],
        [0.35, 0.36, 0.39, 0.38, 0.37, 0.42, 0.35, 0.25, 0.35, 0.37, 0.35, 1.00],
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
creditNonQ_corr = [0.87,0.50,0.5]

# p.18, 49: Correlation between non-residual bucket
cr_gamma_diff_ccy = 0.79

# p.20, 56: Risk Weights for Equity Risk Class
equity_rw = {
    1:  29,
    2:  30,
    3:  28,
    4:  28,
    5:  23,
    6:  23,
    7:  26,
    8:  29,
    9:  32,
    10: 39,
    11: 17,
    12: 17,
    0:  39, # Residual
}

# p.20, 57: Historical Volatility Ratio for Equity Risk Class
equity_hvr = 0.57

# p.20, 58: Vega Risk Weight for Equity Risk Class
equity_vrw = 0.29
equity_vrw_bucket_12 = 0.71

# p.20, 59: Correlations for Equity Risk Class
equity_corr = {
    1:  0.13,
    2:  0.16,
    3:  0.24,
    4:  0.20,
    5:  0.21,
    6:  0.30,
    7:  0.32,
    8:  0.34,
    9:  0.28,
    10: 0.21,
    11: 0.46,
    12: 0.46,
    0:  0,   # Residual
}

# p.20, 60: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
equity_corr_non_res = list(
    zip(
        [1.00, 0.14, 0.16, 0.15, 0.12, 0.14, 0.14, 0.14, 0.14, 0.11, 0.17, 0.17],
        [0.14, 1.00, 0.19, 0.17, 0.14, 0.17, 0.17, 0.17, 0.18, 0.13, 0.20, 0.20],
        [0.16, 0.19, 1.00, 0.19, 0.14, 0.18, 0.21, 0.18, 0.20, 0.14, 0.21, 0.21],
        [0.15, 0.17, 0.19, 1.00, 0.17, 0.21, 0.21, 0.22, 0.20, 0.17, 0.25, 0.25],
        [0.12, 0.14, 0.14, 0.17, 1.00, 0.24, 0.22, 0.25, 0.15, 0.19, 0.29, 0.29],
        [0.14, 0.17, 0.18, 0.21, 0.24, 1.00, 0.29, 0.31, 0.20, 0.24, 0.34, 0.34],
        [0.14, 0.17, 0.21, 0.21, 0.22, 0.29, 1.00, 0.29, 0.20, 0.23, 0.33, 0.33],
        [0.14, 0.17, 0.18, 0.22, 0.25, 0.31, 0.29, 1.00, 0.20, 0.24, 0.37, 0.37],
        [0.14, 0.18, 0.20, 0.20, 0.15, 0.20, 0.20, 0.20, 1.00, 0.16, 0.23, 0.23],
        [0.11, 0.13, 0.14, 0.17, 0.19, 0.24, 0.23, 0.24, 0.16, 1.00, 0.25, 0.25],
        [0.17, 0.20, 0.21, 0.25, 0.29, 0.34, 0.33, 0.37, 0.23, 0.25, 1.00, 0.46],
        [0.17, 0.20, 0.21, 0.25, 0.29, 0.34, 0.33, 0.37, 0.23, 0.25, 0.46, 1.00],
    )
)

# p.22, 61: Risk Weights for Commodity Risk Class
commodity_rw = {
    1:  25,
    2:  21,
    3:  23,
    4:  19,
    5:  24,
    6:  27,
    7:  33,
    8:  37,
    9:  64,
    10: 43,
    11: 21,
    12: 19,
    13: 14,
    14: 17,
    15: 11,
    16: 64,
    17: 16,
}

# p.22, 62: Historical Volatility Ratio for Commodity Risk Class
commodity_hvr = 0.89

# p.22, 63: Vega Risk Weight for Commodity Risk Class
commodity_vrw = 0.37

# p.22, 64: Correlations for Commodity Risk Class
commodity_corr = {
    1:  0.83,
    2:  0.98,
    3:  0.98,
    4:  0.98,
    5:  0.98,
    6:  0.94,
    7:  0.94,
    8:  0.37,
    9:  0.58,
    10: 0.50,
    11: 0.61,
    12: 0.62,
    13: 0.57,
    14: 0.14,
    15: 0.16,
    16: 0.00,
    17: 0.34,
}

# p.23, 65: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
commodity_corr_non_res = list(
    zip(
        [1.00, 0.22, 0.17, 0.26, 0.23, 0.30, 0.63, 0.20, 0.42, 0.20, 0.13, 0.10, 0.13, 0.10, 0.02, 0.00, 0.19],
        [0.22, 1.00, 0.94, 0.91, 0.88, 0.25, 0.08, 0.19, 0.10, 0.17, 0.40, 0.29, 0.30, 0.24, 0.17, 0.00, 0.63],
        [0.17, 0.94, 1.00, 0.90, 0.86, 0.19, 0.03, 0.15, 0.06, 0.20, 0.37, 0.26, 0.29, 0.22, 0.16, 0.00, 0.58],
        [0.26, 0.91, 0.90, 1.00, 0.80, 0.28, 0.10, 0.23, 0.13, 0.21, 0.35, 0.19, 0.32, 0.19, 0.15, 0.00, 0.58],
        [0.23, 0.88, 0.86, 0.80, 1.00, 0.18, 0.12, 0.16, 0.08, 0.21, 0.40, 0.31, 0.28, 0.29, 0.18, 0.00, 0.59],
        [0.30, 0.25, 0.19, 0.28, 0.18, 1.00, 0.24, 0.60, 0.16, 0.00, 0.17, 0.07, 0.19, 0.03, 0.13, 0.00, 0.29],
        [0.63, 0.08, 0.03, 0.10, 0.12, 0.24, 1.00, 0.14, 0.70, 0.07, 0.09, 0.08, 0.12, 0.05, 0.01, 0.00, 0.16],
        [0.20, 0.19, 0.15, 0.23, 0.16, 0.60, 0.14, 1.00, 0.14, 0.00, 0.10, 0.03, 0.13, 0.03, 0.06, 0.00, 0.19],
        [0.42, 0.10, 0.06, 0.13, 0.08, 0.16, 0.70, 0.14, 1.00, 0.03, 0.06, -0.02, 0.14, 0.04, 0.01, 0.00, 0.15],
        [0.20, 0.17, 0.20, 0.21, 0.21, 0.00, 0.07, 0.00, 0.03, 1.00, 0.16, 0.10, 0.08, 0.10, 0.01, 0.00, 0.08],
        [0.13, 0.40, 0.37, 0.35, 0.40, 0.17, 0.09, 0.10, 0.06, 0.16, 1.00, 0.41, 0.28, 0.22, 0.18, 0.00, 0.37],
        [0.10, 0.29, 0.26, 0.19, 0.31, 0.07, 0.08, 0.03, -0.02, 0.10, 0.41, 1.00, 0.20, 0.19, 0.10, 0.00, 0.25],
        [0.13, 0.30, 0.29, 0.32, 0.28, 0.19, 0.12, 0.13, 0.14, 0.08, 0.28, 0.20, 1.00, 0.17, 0.16, 0.00, 0.32],
        [0.10, 0.24, 0.22, 0.19, 0.29, 0.03, 0.05, 0.03, 0.04, 0.10, 0.22, 0.19, 0.17, 1.00, 0.13, 0.00, 0.22],
        [0.02, 0.17, 0.16, 0.15, 0.18, 0.13, 0.01, 0.06, 0.01, 0.01, 0.18, 0.10, 0.16, 0.13, 1.00, 0.00, 0.18],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00],
        [0.19, 0.63, 0.58, 0.58, 0.59, 0.29, 0.16, 0.19, 0.15, 0.08, 0.37, 0.25, 0.32, 0.22, 0.18, 0.00, 1.00],
    )
)

# p.24, 67: The group of high FX volatility currencies
high_vol_currency_group = ['ARS', 'EGP', 'ETB', 'GHS', 'LBP', 'NGN', 'RUB', 'SCR', 'VES', 'ZMW']

# p.24, 69: Risk Weights for a currency depends on the group of the calculation currency
fx_rw = {
    "Regular": {
        "Regular": 7.1,
        "High":    18.0,
    },
    "High": {
        "Regular": 18.0,
        "High":    30.6,
    }
}

# p.24, 70: Historical Volatility Ratio for FX Risk Class
fx_hvr = 0.68

# p.24, 71: Vega Risk Weight for FX Risk Class
fx_vrw = 0.34

# p.24, 72: Correlations for FX
## Regular Vol FX Group
fx_reg_vol_corr = {
    "Regular": {
        "Regular": 0.50,
        "High":    0.20,
    },
    "High": {
        "Regular": 0.20,
        "High":    0.08,
    }
}

# p.25, 72: Correlations for FX Risk Factor
# High Vol FX Group
fx_high_vol_corr = {
    "Regular": {
        "Regular": 0.92,
        "High":    0.68,
    },
    "High": {
        "Regular": 0.68,
        "High":    0.50,
    }
}

# p.25, 73: Correlations for FX Volatility&Curvature Risk Factor
fx_vega_corr = 0.5

# p.26, 74&75: Delta Concentration Thresholds for Interest Rate Risk
ir_delta_CT = {
    'Others' : 51,   # All other currencies
    'USD'    : 210,  # Regular volatility, well-traded
    'EUR'    : 210,  # Regular volatility, well-traded
    'GBP'    : 210,  # Regular volatility, well-traded
    'AUD'    : 100,  # Regular volatility, less well-traded
    'CAD'    : 100,  # Regular volatility, less well-traded
    'CHF'    : 100,  # Regular volatility, less well-traded
    'DKK'    : 100,  # Regular volatility, less well-traded
    'HKD'    : 100,  # Regular volatility, less well-traded
    'KRW'    : 100,  # Regular volatility, less well-traded
    'NOK'    : 100,  # Regular volatility, less well-traded
    'NZD'    : 100,  # Regular volatility, less well-traded
    'SEK'    : 100,  # Regular volatility, less well-traded
    'SGD'    : 100,  # Regular volatility, less well-traded
    'TWD'    : 100,  # Regular volatility, less well-traded
    'JPY'    : 230,  # Low volatility
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
        1 : 4.2,  # Investment Grades(RMBS & CMBS)
        2 : 0.19, # High Yield/Non-rated (RMBS & CMBS)
        0 : 0.19, # Residual
    }
}

# p.26, 77: Delta Concentration Thresholds for Equity Risk
equity_delta_CT = {
    1 : 2.8,   # Emerging Markets  - Large Cap
    2 : 2.8,   # Emerging Markets  - Large Cap
    3 : 2.8,   # Emerging Markets  - Large Cap
    4 : 2.8,   # Emerging Markets  - Large Cap
    5 : 14,    # Developed Markets - Large Cap
    6 : 14,    # Developed Markets - Large Cap
    7 : 14,    # Developed Markets - Large Cap
    8 : 14,    # Developed Markets - Large Cap
    9 : 0.7,   # Emerging Markets  - Small Cap
    10: 0.33,  # Developed Markets - Small Cap
    11: 730,   # Indexes, Funds, ETFs, Volatility Indexes
    12: 730,   # Indexes, Funds, ETFs, Volatility Indexes
    0 : 0.33,  # Residual - Not classified
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
    8 : 1800, # Power
    9 : 1800, # Power
    10: 52,   # Freight, Dry or Wet
    11: 530,  # Base metals
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
    'Category1' : 3100, # Significantly material
    'Category2' : 950,  # Frequently traded
    'Others'    : 160,  # All other currencies
}

# p.27, 81: Vega Concentration Thresholds for IR Risk
ir_vega_CT = {
    'Others' : 110,  # All other currencies
    'USD'    : 4400, # Regular volatility, well-traded
    'EUR'    : 4400, # Regular volatility, well-traded
    'GBP'    : 4400, # Regular volatility, well-traded
    'AUD'    : 480,  # Regular volatility, less well-traded
    'CAD'    : 480,  # Regular volatility, less well-traded
    'CHF'    : 480,  # Regular volatility, less well-traded
    'DKK'    : 480,  # Regular volatility, less well-traded
    'HKD'    : 480,  # Regular volatility, less well-traded
    'KRW'    : 480,  # Regular volatility, less well-traded
    'NOK'    : 480,  # Regular volatility, less well-traded
    'NZD'    : 480,  # Regular volatility, less well-traded
    'SEK'    : 480,  # Regular volatility, less well-traded
    'SGD'    : 480,  # Regular volatility, less well-traded
    'TWD'    : 480,  # Regular volatility, less well-traded
    'JPY'    : 860,  # Low volatility
}

# p.27, 83: Vega Concentration Thresholds for Credit Spread Risk
credit_vega_CT = {
    "Qualifying"     : 270,
    "Non-Qualifying" : 22,
}

# p.28, 84: Vega Concentration Thresholds for Equity Risk
equity_vega_CT = {
    1 : 270,  # Emerging Markets  - Large Cap
    2 : 270,  # Emerging Markets  - Large Cap
    3 : 270,  # Emerging Markets  - Large Cap
    4 : 270,  # Emerging Markets  - Large Cap
    5 : 780,  # Developed Markets - Large Cap
    6 : 780,  # Developed Markets - Large Cap
    7 : 780,  # Developed Markets - Large Cap
    8 : 780,  # Developed Markets - Large Cap
    9 : 84,   # Emerging Markets  - Small Cap
    10: 290,  # Developed Markets - Small Cap
    11: 3200, # Indexes, Funds, ETFs, Volatility Indexes
    12: 3200, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 84,   # Residual - Not classified
}

# p.28, 85: Vega Concentration Thresholds for Commodity Risk
commodity_vega_CT = {
    1 : 480,  # Coal
    2 : 2400, # Crude Oil
    3 : 250,  # Oil Fractions
    4 : 250,  # Oil Fractions
    5 : 250,  # Oil Fractions
    6 : 7000, # Natural Gas
    7 : 7000, # Natural Gas
    8 : 1300, # Power
    9 : 1300, # Power
    10: 100,  # Freight, Dry or Wet
    11: 520,  # Base metals
    12: 740,  # Precious Metals
    13: 790,  # Agricultural
    14: 790,  # Agricultural
    15: 790,  # Agricultural
    16: 62,   # Other
    17: 62,   # Indices
}

# p.28, 86: Vega Concentration Thresholds for FX Risk
fx_vega_CT = {
    'Category1-Category1' : 2800,
    'Category1-Category2' : 1400,
    'Category1-Category3' : 740,
    'Category2-Category2' : 670,
    'Category2-Category3' : 440,
    'Category3-Category3' : 270,
}

# p.29, 88: Correlation between Risk Classes within Product Classes
corr_params = list(
    zip(
        [1.00, 0.10, 0.14, 0.12, 0.30, 0.10],
        [0.10, 1.00, 0.60, 0.66, 0.25, 0.22],
        [0.14, 0.60, 1.00, 0.52, 0.27, 0.15],
        [0.12, 0.66, 0.52, 1.00, 0.33, 0.24],
        [0.30, 0.25, 0.27, 0.33, 1.00, 0.23],
        [0.10, 0.22, 0.15, 0.24, 0.23, 1.00],
    )
)
