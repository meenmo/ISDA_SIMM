# The parameters below can be found at https://www.isda.org/a/b4ugE/ISDA-SIMM_v2.7_PUBLIC.pdf

# p.14, 33
## Regular/Low Vol Currency Buckets
reg_vol_ccy_bucket = ['USD', 'EUR', 'GBP', 'CHF', 'AUD', 'NZD', 'CAD', 'SEK', 'NOK', 'DKK', 'HKD', 'KRW', 'SGD', 'TWD']
low_vol_ccy_bucket = ['JPY']

## table1: Risk Weights for Regular/Low/High Vol Currency Bucket Respectively
reg_vol_rw = {
    '2w'  : 109,
    '1m'  : 106,
    '3m'  : 91,
    '6m'  : 69,
    '1y'  : 68,
    '2y'  : 68,
    '3y'  : 66,
    '5y'  : 61,
    '10y' : 59,
    '15y' : 56,
    '20y' : 57,
    '30y' : 65,
}

low_vol_rw = {
    '2w'  : 15, 
    '1m'  : 21, 
    '3m'  : 10,
    '6m'  : 10,
    '1y'  : 11,
    '2y'  : 15,
    '3y'  : 18,
    '5y'  : 23,
    '10y' : 25,
    '15y' : 23,
    '20y' : 23,
    '30y' : 25,
}

high_vol_rw = {
    '2w'  : 171,
    '1m'  : 102,
    '3m'  : 94,
    '6m'  : 96,
    '1y'  : 105,
    '2y'  : 96,
    '3y'  : 99,
    '5y'  : 93,
    '10y' : 99,
    '15y' : 100,
    '20y' : 101,
    '30y' : 96,
}

## Risk Weights for Any Currency's Inflation Rate/Cross-Currency Basis Swap Spread
inflation_rw = 52
ccy_basis_swap_spread_rw = 21

# p.14, 34: The Historical Volatility Ratio for the Interest Rate Risk Class
ir_hvr = 0.69

# p.14, 35: The Vega Risk Weight for the Interest Rate Risk Class
ir_vrw = 0.20

# p.15, 36: IR - Correlations
## Correlations for Aggregated Weighted Sensitivities/Risk Exposures
ir_corr = list(
    zip(
        [1.00, 0.75, 0.67, 0.57, 0.43, 0.33, 0.28, 0.24, 0.19, 0.17, 0.16, 0.15],
        [0.75, 1.00, 0.85, 0.72, 0.52, 0.38, 0.30, 0.24, 0.19, 0.14, 0.16, 0.15],
        [0.67, 0.85, 1.00, 0.88, 0.67, 0.52, 0.44, 0.37, 0.30, 0.23, 0.21, 0.21],
        [0.57, 0.72, 0.88, 1.00, 0.86, 0.73, 0.64, 0.56, 0.47, 0.41, 0.38, 0.37],
        [0.43, 0.52, 0.67, 0.86, 1.00, 0.94, 0.86, 0.78, 0.67, 0.61, 0.57, 0.56],
        [0.33, 0.38, 0.52, 0.73, 0.94, 1.00, 0.96, 0.91, 0.80, 0.74, 0.70, 0.69],
        [0.28, 0.30, 0.44, 0.64, 0.86, 0.96, 1.00, 0.97, 0.87, 0.81, 0.77, 0.76],
        [0.24, 0.24, 0.37, 0.56, 0.78, 0.91, 0.97, 1.00, 0.94, 0.90, 0.86, 0.85],
        [0.19, 0.19, 0.30, 0.47, 0.67, 0.80, 0.87, 0.94, 1.00, 0.97, 0.94, 0.94],
        [0.17, 0.14, 0.23, 0.41, 0.61, 0.74, 0.81, 0.90, 0.97, 1.00, 0.97, 0.97],
        [0.16, 0.12, 0.21, 0.38, 0.57, 0.70, 0.77, 0.86, 0.94, 0.97, 1.00, 0.99],
        [0.15, 0.12, 0.21, 0.37, 0.56, 0.69, 0.76, 0.85, 0.94, 0.97, 0.99, 1.00],
    )
)
## The Correlation between any two sub-curves of the same currency
sub_curves_corr = 0.99
inflation_corr  = 0.26
ccy_basis_spread_corr = -0.05

# p.15, 37: The parameter for aggregating across different currencies
ir_gamma_diff_ccy = 0.30

# p.16, 39: Risk Weights for Credit Qualifying
creditQ_rw = {
    1:  69,
    2:  75,
    3:  69,
    4:  47,
    5:  58,
    6:  48,
    7:  153,
    8:  363,
    9:  156,
    10: 188,
    11: 299,
    12: 119,
    0:  363, # Residual
}

# p.17, 40: Vega Risk Weight for Credit Qualifying
creditQ_vrw = 0.29

# p.17, 41: Base Correlation Weight
base_corr_weight = 9.9

# p.17, 42: Credit Qualifying Correlations
# aggregate sensitivities for same issuer, aggregate sensitivities for different issuer, residual bucket, Base corr across different index families
creditQ_corr = [0.94,0.47,0.5,0.31]

# p.17, 43: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
creditQ_corr_non_res = list(
    zip(
        [1.00, 0.41, 0.39, 0.35, 0.38, 0.36, 0.43, 0.29, 0.36, 0.36, 0.36, 0.37],
        [0.41, 1.00, 0.48, 0.45, 0.48, 0.45, 0.40, 0.35, 0.43, 0.43, 0.42, 0.44],
        [0.39, 0.48, 1.00, 0.49, 0.50, 0.50, 0.41, 0.32, 0.46, 0.45, 0.43, 0.48],
        [0.35, 0.45, 0.49, 1.00, 0.50, 0.49, 0.38, 0.30, 0.42, 0.44, 0.41, 0.47],
        [0.38, 0.48, 0.50, 0.50, 1.00, 0.51, 0.40, 0.31, 0.44, 0.45, 0.43, 0.49],
        [0.36, 0.45, 0.50, 0.49, 0.51, 1.00, 0.39, 0.29, 0.42, 0.43, 0.41, 0.49],
        [0.43, 0.40, 0.41, 0.38, 0.40, 0.39, 1.00, 0.28, 0.37, 0.38, 0.37, 0.39],
        [0.29, 0.35, 0.32, 0.30, 0.31, 0.29, 0.28, 1.00, 0.30, 0.30, 0.29, 0.31],
        [0.36, 0.43, 0.46, 0.42, 0.44, 0.42, 0.37, 0.30, 1.00, 0.42, 0.40, 0.44],
        [0.36, 0.43, 0.45, 0.44, 0.45, 0.43, 0.38, 0.30, 0.42, 1.00, 0.40, 0.45],
        [0.36, 0.42, 0.43, 0.41, 0.43, 0.41, 0.37, 0.29, 0.40, 0.40, 1.00, 0.42],
        [0.37, 0.44, 0.48, 0.47, 0.49, 0.49, 0.39, 0.31, 0.44, 0.45, 0.42, 1.00],
    )
)
# p.18, 46: Risk Weights for Credit Non-Qualifying
creiditNonQ_rw = {
    1: 280,
    2: 2900,
    0: 2900, # Residual
}

# p.18, 47: Vega Risk Weight for Credit Non-Qualifying
creditNonQ_vrw = 0.29

# p.18, 48: Credit Non-Qualifying Correlations
creditNonQ_corr = [0.85,0.29,0.5]

# p.18, 49: Correlation between non-residual bucket
cr_gamma_diff_ccy = 0.51

# p.20, 56: Risk Weights for Equity Risk Class
equity_rw = {
    1:  27,
    2:  30,
    3:  31,
    4:  27,
    5:  23,
    6:  24,
    7:  26,
    8:  27,
    9:  33,
    10: 39,
    11: 15,
    12: 15,
    0:  39, # Residual
}

# p.20, 57: Historical Volatility Ratio for Equity Risk Class
equity_hvr = 0.62

# p.20, 58: Vega Risk Weight for Equity Risk Class 
equity_vrw = 0.25
equity_vrw_bucket_12 = 0.56

# p.20, 59: Correlations for Equity Risk Class
equity_corr = {
    1:  0.14,
    2:  0.16,
    3:  0.23,
    4:  0.21,
    5:  0.23,
    6:  0.32,
    7:  0.32,
    8:  0.35,
    9:  0.21,
    10: 0.22,
    11: 0.40,
    12: 0.40,
    0:  0,   # Residual
}

# p.20, 60: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
equity_corr_non_res = list(
    zip(
        [1.00, 0.14, 0.15, 0.16, 0.13, 0.15, 0.14, 0.15, 0.14, 0.12, 0.17, 0.17],
        [0.14, 1.00, 0.18, 0.18, 0.14, 0.17, 0.17, 0.18, 0.16, 0.14, 0.19, 0.19],
        [0.15, 0.18, 1.00, 0.19, 0.14, 0.18, 0.21, 0.19, 0.18, 0.14, 0.21, 0.21],
        [0.16, 0.18, 0.19, 1.00, 0.17, 0.22, 0.21, 0.23, 0.18, 0.17, 0.24, 0.24],
        [0.13, 0.14, 0.14, 0.17, 1.00, 0.25, 0.23, 0.26, 0.13, 0.20, 0.28, 0.28],
        [0.15, 0.17, 0.18, 0.22, 0.25, 1.00, 0.29, 0.33, 0.16, 0.26, 0.34, 0.34],
        [0.14, 0.17, 0.21, 0.21, 0.23, 0.29, 1.00, 0.30, 0.15, 0.24, 0.33, 0.33],
        [0.15, 0.18, 0.19, 0.23, 0.26, 0.33, 0.30, 1.00, 0.16, 0.26, 0.37, 0.37],
        [0.14, 0.16, 0.18, 0.18, 0.13, 0.16, 0.15, 0.16, 1.00, 0.12, 0.19, 0.19],
        [0.12, 0.14, 0.14, 0.17, 0.20, 0.26, 0.24, 0.26, 0.12, 1.00, 0.26, 0.26],
        [0.17, 0.19, 0.21, 0.24, 0.28, 0.34, 0.33, 0.37, 0.19, 0.26, 1.00, 0.40],
        [0.17, 0.19, 0.21, 0.24, 0.28, 0.34, 0.33, 0.37, 0.19, 0.26, 0.40, 1.00],
    )
)

# p.22, 61: Risk Weights for Commodity Risk Class
commodity_rw = {
    1:  48,
    2:  21,
    3:  23,
    4:  20,
    5:  24,
    6:  33,
    7:  61,
    8:  45,
    9:  65,
    10: 45,
    11: 21,
    12: 19,
    13: 16,
    14: 16,
    15: 11,
    16: 65,
    17: 16,
}

# p.22, 62: Historical Volatility Ratio for Commodity Risk Class
commodity_hvr = 0.85

# p.22, 63: Vega Risk Weight for Commodity Risk Class
commodity_vrw = 0.34

# p.22, 64: Correlations for Commodity Risk Class
commodity_corr = {
    1:  0.84,
    2:  0.98,
    3:  0.98,
    4:  0.98,
    5:  0.98,
    6:  0.93,
    7:  0.93,
    8:  0.51,
    9:  0.59,
    10: 0.44,
    11: 0.58,
    12: 0.60,
    13: 0.60,
    14: 0.21,
    15: 0.17,
    16: 0.00,
    17: 0.43,
}

# p.23, 65: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
commodity_corr_non_res = list(
    zip(
        [1.00, 0.23, 0.19, 0.28, 0.24, 0.32, 0.62, 0.29, 0.50, 0.15, 0.13, 0.08, 0.19, 0.12, 0.04, 0.00, 0.22],
        [0.23, 1.00, 0.94, 0.92, 0.89, 0.36, 0.15, 0.23, 0.15, 0.20, 0.42, 0.31, 0.38, 0.28, 0.16, 0.00, 0.67],
        [0.19, 0.94, 1.00, 0.91, 0.86, 0.32, 0.11, 0.19, 0.12, 0.22, 0.41, 0.31, 0.37, 0.25, 0.15, 0.00, 0.64],
        [0.28, 0.92, 0.91, 1.00, 0.81, 0.40, 0.17, 0.26, 0.18, 0.20, 0.41, 0.26, 0.34, 0.25, 0.14, 0.00, 0.64],
        [0.24, 0.89, 0.86, 0.81, 1.00, 0.29, 0.17, 0.26, 0.23, 0.26, 0.42, 0.34, 0.23, 0.32, 0.14, 0.00, 0.62],
        [0.32, 0.36, 0.32, 0.40, 0.29, 1.00, 0.30, 0.66, 0.23, 0.07, 0.12, 0.07, 0.23, 0.09, 0.11, 0.00, 0.39],
        [0.62, 0.15, 0.11, 0.17, 0.17, 0.30, 1.00, 0.19, 0.78, 0.12, 0.12, 0.02, 0.11, 0.07, 0.00, 0.00, 0.21],
        [0.29, 0.23, 0.19, 0.26, 0.21, 0.66, 0.19, 1.00, 0.19, 0.04, 0.10, -0.01, 0.11, 0.04, 0.03, 0.00, 0.21],
        [0.50, 0.15, 0.12, 0.18, 0.23, 0.23, 0.78, 0.19, 1.00, 0.07, 0.06, -0.08, 0.13, 0.12, 0.10, 0.00, 0.18],
        [0.15, 0.20, 0.22, 0.20, 0.26, 0.07, 0.12, 0.04, 0.07, 1.00, 0.19, 0.10, 0.13, 0.10, 0.10, 0.00, 0.12],
        [0.13, 0.42, 0.41, 0.41, 0.42, 0.21, 0.12, 0.10, 0.06, 0.19, 1.00, 0.39, 0.31, 0.24, 0.14, 0.00, 0.39],
        [0.08, 0.31, 0.31, 0.26, 0.34, 0.07, 0.02, -0.01, -0.08, 0.10, 0.39, 1.00, 0.22, 0.20, 0.12, 0.00, 0.28],
        [0.19, 0.38, 0.37, 0.34, 0.23, 0.19, 0.11, 0.11, 0.13, 0.13, 0.31, 0.22, 1.00, 0.28, 0.19, 0.00, 0.41],
        [0.12, 0.28, 0.25, 0.27, 0.32, 0.09, 0.07, 0.04, 0.12, 0.10, 0.24, 0.20, 0.28, 1.00, 0.09, 0.00, 0.22],
        [0.04, 0.16, 0.15, 0.14, 0.14, 0.11, 0.00, 0.03, 0.10, 0.10, 0.14, 0.12, 0.19, 0.09, 1.00, 0.00, 0.21],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00],
        [0.22, 0.67, 0.64, 0.64, 0.62, 0.39, 0.21, 0.21, 0.18, 0.12, 0.39, 0.28, 0.41, 0.22, 0.21, 0.00, 1.00],
    )
)

# p.24, 67: The group of high FX volatility currencies
high_vol_currency_group = ['ARS', 'RUB', 'TRY']

# p.24, 69: Risk Weights for a currency depends on the group of the calculation currency
fx_rw = {
    "Regular": {
        "Regular": 7.3,
        "High":    21.4,
    },
    "High": {
        "Regular": 21.4,
        "High":    35.9,
    }
}

# p.24, 70: Historical Volatility Ratio for FX Risk Class
fx_hvr = 0.62

# p.24, 71: Vega Risk Weight for FX Risk Class
fx_vrw = 0.35

# p.24, 72: Correlations for FX
## Regular Vol FX Group
fx_reg_vol_corr = {
    "Regular": {
        "Regular": 0.50,
        "High":    0.17,
    },
    "High": {
        "Regular": 0.17,
        "High":   -0.41,
    }
}

# p.25, 72: Correlations for FX Risk Factor
# High Vol FX Group
fx_high_vol_corr = {
    "Regular": {
        "Regular": 0.94,
        "High":    0.84,
    },
    "High": {
        "Regular": 0.84,
        "High":    0.50,
    }
}

# p.25, 73: Correlations for FX Volatility&Curvature Risk Factor
fx_vega_corr = 0.5 

# p.26, 74&75: Delta Concentration Thresholds for Interest Rate Risk
ir_delta_CT = {
    'Others' : 29,   # All other currencies
    'USD'    : 340,  # Regular volatility, well-traded 
    'EUR'    : 340,  # Regular volatility, well-traded 
    'GBP'    : 340,  # Regular volatility, well-traded
    'AUD'    : 61,  # Regular volatility, less well-traded 
    'CAD'    : 61,  # Regular volatility, less well-traded 
    'CHF'    : 61,  # Regular volatility, less well-traded 
    'DKK'    : 61,  # Regular volatility, less well-traded 
    'HKD'    : 61,  # Regular volatility, less well-traded 
    'KRW'    : 61,  # Regular volatility, less well-traded 
    'NOK'    : 61,  # Regular volatility, less well-traded 
    'NZD'    : 61,  # Regular volatility, less well-traded 
    'SEK'    : 61,  # Regular volatility, less well-traded 
    'SGD'    : 61,  # Regular volatility, less well-traded 
    'TWD'    : 61,  # Regular volatility, less well-traded
    'JPY'    : 150,   # Low volatility
}

# p.26, 76: Delta Concentration Thresholds for Credit Spread Risk Group
credit_delta_CT = {
    "Qualifying" : {
        1 : 0.98, # Sovereigns including central banks
        2 : 0.18, # Corporate entities 
        3 : 0.18, # Corporate entities
        4 : 0.18, # Corporate entities
        5 : 0.18, # Corporate entities
        6 : 0.18, # Corporate entities
        7 : 0.98, # Sovereigns including central banks
        8 : 0.18, # Corporate entities
        9 : 0.18, # Corporate entities
        10: 0.18, # Corporate entities
        11: 0.18, # Corporate entities
        12: 0.18, # Corporate entities
        0 : 0.18, # Residual
    }, 
    "Non-Qualifying" : {
        1 : 3.3, # Investment Grades(RMBS & CMBS) 
        2 : 0.18, # High Yield/Non-rated (RMBS & CMBS)
        0 : 0.18, # Residual
    }
}

# p.26, 77: Delta Concentration Thresholds for Equity Risk
equity_delta_CT = {
    1 : 2.5,     # Emerging Markets  - Large Cap
    2 : 2.5,     # Emerging Markets  - Large Cap
    3 : 2.5,     # Emerging Markets  - Large Cap
    4 : 2.5,     # Emerging Markets  - Large Cap
    5 : 10,    # Developed Markets - Large Cap
    6 : 10,    # Developed Markets - Large Cap
    7 : 10,    # Developed Markets - Large Cap
    8 : 10,    # Developed Markets - Large Cap
    9 : 0.61,  # Emerging Markets  - Small Cap
    10: 0.3,  # Developed Markets - Small Cap
    11: 710,   # Indexes, Funds, ETFs, Volatility Indexes
    12: 710,   # Indexes, Funds, ETFs, Volatility Indexes
    0 : 0.3,  # Residual - Not classified
}

# p.27, 78: Delta Concentration Thresholds for Commodity Risk
commodity_delta_CT = {
    1 : 310,  # Coal
    2 : 2500, # Crude Oil
    3 : 1700, # Oil Fractions 
    4 : 1700, # Oil Fractions 
    5 : 1700, # Oil Fractions 
    6 : 2400, # Natural Gas 
    7 : 2400, # Natural Gas 
    8 : 1800, # Power 
    9 : 1800, # Power 
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
    'Category1' : 2000, # Significantly material 
    'Category2' : 630,  # Frequently traded 
    'Others'    : 120,  # All other currencies
}

# p.27, 81: Vega Concentration Thresholds for IR Risk
ir_vega_CT = {
    'Others' : 76,   # All other currencies
    'USD'    : 4900, # Regular volatility, well-traded 
    'EUR'    : 4900, # Regular volatility, well-traded 
    'GBP'    : 4900, # Regular volatility, well-traded
    'AUD'    : 550,  # Regular volatility, less well-traded 
    'CAD'    : 550,  # Regular volatility, less well-traded 
    'CHF'    : 550,  # Regular volatility, less well-traded 
    'DKK'    : 550,  # Regular volatility, less well-traded 
    'HKD'    : 550,  # Regular volatility, less well-traded 
    'KRW'    : 550,  # Regular volatility, less well-traded 
    'NOK'    : 550,  # Regular volatility, less well-traded 
    'NZD'    : 550,  # Regular volatility, less well-traded 
    'SEK'    : 550,  # Regular volatility, less well-traded 
    'SGD'    : 550,  # Regular volatility, less well-traded 
    'TWD'    : 550,  # Regular volatility, less well-traded
    'JPY'    : 890,  # Low volatility
}

# p.27, 83: Vega Concentration Thresholds for Credit Spread Risk
credit_vega_CT = {
    "Qualifying"     : 290, 
    "Non-Qualifying" : 21,
}

# p.28, 84: Vega Concentration Thresholds for Equity Risk
equity_vega_CT = {
    1 : 300,  # Emerging Markets  - Large Cap
    2 : 300,  # Emerging Markets  - Large Cap
    3 : 300,  # Emerging Markets  - Large Cap
    4 : 300,  # Emerging Markets  - Large Cap
    5 : 1500, # Developed Markets - Large Cap
    6 : 1500, # Developed Markets - Large Cap
    7 : 1500, # Developed Markets - Large Cap
    8 : 1500, # Developed Markets - Large Cap
    9 : 74,   # Emerging Markets  - Small Cap
    10: 280,  # Developed Markets - Small Cap
    11: 4300, # Indexes, Funds, ETFs, Volatility Indexes
    12: 4300, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 74,   # Residual - Not classified
}

# p.28, 85: Vega Concentration Thresholds for Commodity Risk
commodity_vega_CT = {
    1 : 450,  # Coal
    2 : 2300, # Crude Oil
    3 : 240,  # Oil Fractions 
    4 : 240,  # Oil Fractions 
    5 : 240,  # Oil Fractions 
    6 : 6400, # Natural Gas 
    7 : 6400, # Natural Gas 
    8 : 1300,  # Power 
    9 : 1300,  # Power 
    10: 94,  # Freight, Dry or Wet 
    11: 490,  # Base metals 
    12: 810,  # Precious Metals 
    13: 730,  # Agricultural 
    14: 730,  # Agricultural 
    15: 730,  # Agricultural 
    16: 59,   # Other 
    17: 59,   # Indices 
}

# p.28, 86: Vega Concentration Thresholds for FX Risk
fx_vega_CT = {
    'Category1-Category1' : 3000,
    'Category1-Category2' : 1500,
    'Category1-Category3' : 670,
    'Category2-Category2' : 600,
    'Category2-Category3' : 390,
    'Category3-Category3' : 240,
}

# p.29, 88: Correlation between Risk Classes within Product Classes
corr_params = list(
    zip(
        [1.00, 0.15, 0.09, 0.08, 0.33, 0.09],
        [0.15, 1.00, 0.52, 0.67, 0.23, 0.20],
        [0.09, 0.52, 1.00, 0.36, 0.16, 0.12],
        [0.08, 0.67, 0.36, 1.00, 0.34, 0.24],
        [0.33, 0.23, 0.16, 0.34, 1.00, 0.28],
        [0.09, 0.20, 0.12, 0.24, 0.28, 1.00],
    )
)