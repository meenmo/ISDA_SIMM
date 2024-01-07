# The parameters below can be found at https://www.isda.org/a/oDHTE/ISDA-SIMM-v2.3-PUBLIC.pdf

# p.14, 33
## Regular/Low Vol Currency Buckets
reg_vol_ccy_bucket = ['USD', 'EUR', 'GBP', 'CHF', 'AUD', 'NZD', 'CAD', 'SEK', 'NOK', 'DKK', 'HKD', 'KRW', 'SGD', 'TWD']
low_vol_ccy_bucket = ['JPY']

## table1: Risk Weights for Regular/Low/High Vol Currency Bucket Respectively
reg_vol_rw = {
    '2w'  : 114,
    '1m'  : 107,
    '3m'  : 95,
    '6m'  : 71,
    '1y'  : 56,
    '2y'  : 53,
    '3y'  : 50,
    '5y'  : 51,
    '10y' : 53,
    '15y' : 50,
    '20y' : 54,
    '30y' : 63,
}

low_vol_rw = {
    '2w'  : 15, 
    '1m'  : 21, 
    '3m'  : 10,
    '6m'  : 10,
    '1y'  : 11,
    '2y'  : 15,
    '3y'  : 18,
    '5y'  : 19,
    '10y' : 19,
    '15y' : 18,
    '20y' : 20,
    '30y' : 22,
}

high_vol_rw = {
    '2w'  : 103, 
    '1m'  : 96, 
    '3m'  : 84,
    '6m'  : 84,
    '1y'  : 89,
    '2y'  : 87,
    '3y'  : 90,
    '5y'  : 89,
    '10y' : 90,
    '15y' : 99,
    '20y' : 100,
    '30y' : 96,
}

## Risk Weights for Any Currency's Inflation Rate/Cross-Currency Basis Swap Spread
inflation_rw = 50
ccy_basis_swap_spread_rw = 22

# p.14, 34: The Historical Volatility Ratio for the Interest Rate Risk Class
ir_hvr = 0.49

# p.14, 35: The Vega Risk Weight for the Interest Rate Risk Class
ir_vrw = 0.16

# p.15, 36: IR - Correlations
## Correlations for Aggregated Weighted Sensitivities/Risk Exposures
ir_corr = list(
    zip(
        [1.00,0.73,0.64,0.57,0.44,0.34,0.29,0.24,0.18,0.13,0.11,0.09],
        [0.73,1.00,0.78,0.67,0.5,0.37,0.3,0.24,0.18,0.13,0.11,0.1],
        [0.64,0.78,1.00,0.85,0.66,0.52,0.43,0.35,0.27,0.2,0.17,0.17],
        [0.57,0.67,0.85,1.00,0.81,0.68,0.59,0.5,0.41,0.35,0.33,0.31],
        [0.44,0.5,0.66,0.81,1.00,0.94,0.85,0.76,0.65,0.59,0.56,0.54],
        [0.34,0.37,0.52,0.68,0.94,1.00,0.95,0.89,0.79,0.75,0.72,0.7],
        [0.29,0.3,0.43,0.59,0.85,0.95,1.00,0.96,0.88,0.83,0.8,0.78],
        [0.24,0.24,0.35,0.5,0.76,0.89,0.96,1.00,0.95,0.91,0.88,0.87],
        [0.18,0.18,0.27,0.41,0.65,0.79,0.88,0.95,1.00,0.97,0.95,0.95],
        [0.13,0.13,0.2,0.35,0.59,0.75,0.83,0.91,0.97,1.00,0.98,0.98],
        [0.11,0.11,0.17,0.33,0.56,0.72,0.8,0.88,0.95,0.98,1.00,0.99],
        [0.09,0.1,0.17,0.31,0.54,0.7,0.78,0.87,0.95,0.98,0.99,1],
    )
)
## The Correlation between any two sub-curves of the same currency
sub_curves_corr = 0.986
inflation_corr  = 0.42
ccy_basis_spread_corr = 0.04

# p.15, 37: The parameter for aggregating across different currencies
ir_gamma_diff_ccy = 0.2

# p.16, 39: Risk Weights for Credit Qualifying
creditQ_rw = {
    0: 333, # Residual
    1: 75,
    2: 89,
    3: 68,
    4: 51,
    5: 50,
    6: 47,
    7: 157,
    8: 333,
    9: 142,
    10: 214,
    11: 143,
    12: 160,
}

# p.17, 40: Vega Risk Weight for Credit Qualifying
creditQ_vrw = 0.46

# p.17, 41: Base Correlation Weight
base_corr_weight = 12

# p.17, 42: Credit Qualifying Correlations
creditQ_corr = [0.94,0.42,0.5,0.18]

# p.17, 43: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
creditQ_corr_non_res = list(
    zip(
        [1.00,0.39,0.39,0.40,0.40,0.37,0.39,0.32,0.35,0.33,0.33,0.30],
        [0.39,1.00,0.43,0.45,0.45,0.43,0.32,0.34,0.39,0.36,0.36,0.31],
        [0.39,0.43,1.00,0.47,0.48,0.45,0.33,0.33,0.41,0.38,0.39,0.35],
        [0.40,0.45,0.47,1.00,0.49,0.47,0.33,0.34,0.41,0.40,0.39,0.34],
        [0.40,0.45,0.48,0.49,1.00,0.48,0.33,0.34,0.41,0.39,0.40,0.34],
        [0.37,0.43,0.45,0.47,0.48,1.00,0.31,0.32,0.38,0.36,0.37,0.32],
        [0.39,0.32,0.33,0.33,0.33,0.31,1.00,0.26,0.31,0.28,0.27,0.25],
        [0.32,0.34,0.33,0.34,0.34,0.32,0.26,1.00,0.31,0.28,0.28,0.25],
        [0.35,0.39,0.41,0.41,0.41,0.38,0.31,0.31,1.00,0.35,0.34,0.32],
        [0.33,0.36,0.38,0.40,0.39,0.36,0.28,0.28,0.35,1.00,0.34,0.29],
        [0.33,0.36,0.39,0.39,0.40,0.37,0.27,0.28,0.34,0.34,1.00,0.30],
        [0.30,0.31,0.35,0.34,0.34,0.32,0.25,0.25,0.32,0.29,0.30,1.00],
    )
)

# p.18, 46: Risk Weights for Credit Non-Qualifying
creiditNonQ_rw = {
    0: 1000,
    1: 240,
    2: 1000,
}

# p.18, 47: Vega Risk Weight for Credit Non-Qualifying
creditNonQ_vrw = 0.46

# p.18, 48: Credit Non-Qualifying Correlations
creditNonQ_corr = [0.77,0.47,0.5]

# p.18, 49: Correlation between non-residual bucket
cr_gamma_diff_ccy = 0.69

# p.20, 56: Risk Weights for Equity Risk Class
equity_rw = {
    0:  29,
    1:  23,
    2:  25,
    3:  29,
    4:  26,
    5:  20,
    6:  21,
    7:  24,
    8:  24,
    9:  29,
    10: 28,
    11: 15,
    12: 15,
}

# p.20, 57: Historical Volatility Ratio for Equity Risk Class
equity_hvr = 0.6

# p.20, 58: Vega Risk Weight for Equity Risk Class 
equity_vrw = 0.26
equity_vrw_bucket_12 = 0.67

# p.20, 59: Correlations for Equity Risk Class
equity_corr = {
    0:  0,
    1:  0.14,
    2:  0.2,
    3:  0.28,
    4:  0.23,
    5:  0.18,
    6:  0.29,
    7:  0.34,
    8:  0.3,
    9:  0.19,
    10: 0.17,
    11: 0.41,
    12: 0.41,
}

# p.20, 60: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
equity_corr_non_res = list(
    zip(
        [1.00,0.17,0.18,0.17,0.11,0.15,0.15,0.15,0.15,0.11,0.19,0.19], 
        [0.17,1.00,0.23,0.21,0.13,0.17,0.18,0.17,0.19,0.13,0.22,0.22], 
        [0.18,0.23,1.00,0.24,0.14,0.19,0.22,0.19,0.20,0.15,0.25,0.25], 
        [0.17,0.21,0.24,1.00,0.14,0.19,0.20,0.19,0.20,0.15,0.24,0.24], 
        [0.11,0.13,0.14,0.14,1.00,0.22,0.21,0.22,0.13,0.16,0.24,0.24], 
        [0.15,0.17,0.19,0.19,0.22,1.00,0.29,0.29,0.17,0.21,0.32,0.32], 
        [0.15,0.18,0.22,0.20,0.21,0.29,1.00,0.28,0.17,0.21,0.34,0.34], 
        [0.15,0.17,0.19,0.19,0.22,0.29,0.28,1.00,0.17,0.21,0.33,0.33], 
        [0.15,0.19,0.20,0.20,0.13,0.17,0.17,0.17,1.00,0.13,0.21,0.21], 
        [0.11,0.13,0.15,0.15,0.16,0.21,0.21,0.21,0.13,1.00,0.22,0.22], 
        [0.19,0.22,0.25,0.24,0.24,0.32,0.34,0.33,0.21,0.22,1.00,0.41], 
        [0.19,0.22,0.25,0.24,0.24,0.32,0.34,0.33,0.21,0.22,0.41,1.00], 
    )
)

# p.22, 61: Risk Weights for Commodity Risk Class
commodity_rw = {
    1:  16,
    2:  20,
    3:  23,
    4:  18,
    5:  28,
    6:  18,
    7:  17,
    8:  57,
    9:  21,
    10: 39,
    11: 20,
    12: 20,
    13: 15,
    14: 15,
    15: 11,
    16: 57,
    17: 16,
}

# p.22, 62: Historical Volatility Ratio for Commodity Risk Class
commodity_hvr = 0.75

# p.22, 63: Vega Risk Weight for Commodity Risk Class
commodity_vrw = 0.41

# p.22, 64: Correlations for Commodity Risk Class
commodity_corr = {
    1:  0.16,
    2:  0.98,
    3:  0.77,
    4:  0.82,
    5:  0.98,
    6:  0.89,
    7:  0.96,
    8:  0.48,
    9:  0.64,
    10: 0.39,
    11: 0.45,
    12: 0.53,
    13: 0.65,
    14: 0.12,
    15: 0.21,
    16: 0,
    17: 0.35,
}

# p.23, 65: Correlations for sensitivity/risk exposure pairs across diffrent non-residual buckets
commodity_corr_non_res = list(
    zip(
        [1.00,0.15,0.15,0.21,0.16,0.03,0.11,0.02,0.12,0.15,0.15,0.06,0,0.04,0.06,0,0.11],
        [0.15,1.00,0.74,0.92,0.89,0.34,0.23,0.16,0.22,0.26,0.31,0.32,0.22,0.25,0.19,0,0.57],
        [0.15,0.74,1.00,0.73,0.69,0.15,0.22,0.08,0.14,0.16,0.21,0.15,-0.03,0.16,0.14,0,0.42],
        [0.21,0.92,0.73,1.00,0.83,0.3,0.26,0.07,0.19,0.22,0.28,0.31,0.13,0.22,0.11,0,0.48],
        [0.16,0.89,0.69,0.83,1.00,0.12,0.14,0,0.06,0.1,0.24,0.2,0.06,0.2,0.09,0,0.49],
        [0.03,0.34,0.15,0.3,0.12,1.00,0.25,0.58,0.21,0.14,0.23,0.15,0.25,0.15,0.12,0,0.37],
        [0.11,0.23,0.22,0.26,0.14,0.25,1.00,0.19,0.64,0.19,0.03,-0.03,0.04,0.05,0.06,0,0.17],
        [0.02,0.16,0.08,0.07,0,0.58,0.19,1.00,0.17,-0.01,0.08,0.01,0.11,0.08,0.08,0,0.15],
        [0.12,0.22,0.14,0.19,0.06,0.21,0.64,0.17,1.00,0.1,0.05,-0.04,0.05,0.03,0.05,0,0.17],
        [0.15,0.26,0.16,0.22,0.1,0.14,0.19,-0.01,0.1,1.00,0.12,0.13,0.12,0.1,0.12,0,0.17],
        [0.15,0.31,0.21,0.28,0.24,0.23,0.03,0.08,0.05,0.12,1.00,0.34,0.23,0.17,0.14,0,0.3],
        [0.06,0.32,0.15,0.31,0.2,0.15,-0.03,0.01,-0.04,0.13,0.34,1.00,0.15,0.19,0.11,0,0.27],
        [0,0.22,-0.03,0.13,0.06,0.25,0.04,0.11,0.05,0.12,0.23,0.15,1.00,0.26,0.14,0,0.26],
        [0.04,0.25,0.16,0.22,0.2,0.15,0.05,0.08,0.03,0.1,0.17,0.19,0.26,1.00,0.1,0,0.22],
        [0.06,0.19,0.14,0.11,0.09,0.12,0.06,0.08,0.05,0.12,0.14,0.11,0.14,0.1,1.00,0,0.2],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.00,0],
        [0.11,0.57,0.42,0.48,0.49,0.37,0.17,0.15,0.17,0.17,0.3,0.27,0.26,0.22,0.2,0,1.00],
    )
)

# p.24, 67: The group of high FX volatility currencies
high_vol_currency_group = []

# p.24, 69: Risk Weights for a currency depends on the group of the calculation currency
fx_rw = {
    # Calculation Currency Group (column)
    "Regular": {
        # Given Currency Group (row)
        "Regular": 7.5,
        "High":    7.5,
    },
    "High": {
        "Regular": 7.5,
        "High":    7.5,
    }
}

# p.24, 70: Historical Volatility Ratio for FX Risk Class
fx_hvr = 0.58

# p.24, 71: Vega Risk Weight for FX Risk Class
fx_vrw = 0.30

# p.24, 72: Correlations for FX
## Regular Vol FX Group
fx_reg_vol_corr = {
    # Calculation Currency Group (column)
    "Regular": {
        # Given Currency Group (row)
        "Regular": 0.5,
        "High":    0.5,
    },
    "High": {
        "Regular": 0.5,
        "High":    0.5,
    }
}

# p.25, 72: Correlations for FX Risk Factor
# High Vol FX Group
fx_high_vol_corr = {
    # Calculation Currency Group (column)
    "Regular": {
        # Given Currency Group (row)
        "Regular": 0.5,
        "High":    0.5,
    },
    "High": {
        "Regular": 0.5,
        "High":    0.5,
    }
}

# p.25, 73: Correlations for FX Volatility&Curvature Risk Factor
fx_vega_corr = 0.5 

# p.26, 74&75: Delta Concentration Thresholds for Interest Rate Risk
ir_delta_CT = {
    'Others' : 31,  # All other currencies
    'USD'    : 220, # Regular volatility, well-traded 
    'EUR'    : 220, # Regular volatility, well-traded 
    'GBP'    : 220, # Regular volatility, well-traded
    'AUD'    : 41,  # Regular volatility, less well-traded 
    'CAD'    : 41,  # Regular volatility, less well-traded 
    'CHF'    : 41,  # Regular volatility, less well-traded 
    'DKK'    : 41,  # Regular volatility, less well-traded 
    'HKD'    : 41,  # Regular volatility, less well-traded 
    'KRW'    : 41,  # Regular volatility, less well-traded 
    'NOK'    : 41,  # Regular volatility, less well-traded 
    'NZD'    : 41,  # Regular volatility, less well-traded 
    'SEK'    : 41,  # Regular volatility, less well-traded 
    'SGD'    : 41,  # Regular volatility, less well-traded 
    'TWD'    : 41,  # Regular volatility, less well-traded
    'JPY'    : 99,  # Low volatility
}

# p.26, 76: Delta Concentration Thresholds for Credit Spread Risk Group
credit_delta_CT = {
    "Qualifying" : {
        1 : 0.95, # Sovereigns including central banks
        2 : 0.18, # Corporate entities 
        3 : 0.18, # Corporate entities
        4 : 0.18, # Corporate entities
        5 : 0.18, # Corporate entities
        6 : 0.18, # Corporate entities
        7 : 0.95, # Sovereigns including central banks
        8 : 0.18, # Corporate entities
        9 : 0.18, # Corporate entities
        10: 0.18, # Corporate entities
        11: 0.18, # Corporate entities
        12: 0.18, # Corporate entities
        0 : 0.18, # Residual
    }, 
    "Non-Qualifying" : {
        1 : 9.5, # Investment Grades(RMBS & CMBS) 
        2 : 0.5, # High Yield/Non-rated (RMBS & CMBS)
        0 : 0.5, # Residual
    }
}

# p.26, 77: Delta Concentration Thresholds for Equity Risk
equity_delta_CT = {
    1 : 7.3,  # Emerging Markets  - Large Cap
    2 : 7.3,  # Emerging Markets  - Large Cap
    3 : 7.3,  # Emerging Markets  - Large Cap
    4 : 7.3,  # Emerging Markets  - Large Cap
    5 : 30,   # Developed Markets - Large Cap
    6 : 30,   # Developed Markets - Large Cap
    7 : 30,   # Developed Markets - Large Cap
    8 : 30,   # Developed Markets - Large Cap
    9 : 2.4,  # Emerging Markets  - Small Cap
    10: 2.4,  # Developed Markets - Small Cap
    11: 1400, # Indexes, Funds, ETFs, Volatility Indexes
    12: 1400, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 2.4,  # Residual - Not classified
}

# p.27, 78: Delta Concentration Thresholds for Commodity Risk
commodity_delta_CT = {
    1 : 310,  # Coal
    2 : 1700, # Crude Oil
    3 : 1300, # Oil Fractions 
    4 : 1300, # Oil Fractions 
    5 : 1300, # Oil Fractions 
    6 : 2800, # Natural Gas 
    7 : 2800, # Natural Gas 
    8 : 2200, # Power 
    9 : 2200, # Power 
    10: 52,   # Freight, Dry or Wet 
    11: 490,  # Base metals 
    12: 1300, # Precious Metals 
    13: 73,   # Agricultural 
    14: 73,   # Agricultural 
    15: 73,   # Agricultural 
    16: 52,   # Other 
    17: 4000, # Indices 
}

# p.27, 80: Currency Categories
fx_category1 = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CHF', 'CAD'] # Significantly material
fx_category2 = ['BRL', 'CNY', 'HKD', 'INR', 'KRW', 'MXN', 'NOK', 'NZD', 'RUB', 'SEK', 'SGD', 'TRY', 'ZAR'] # Frequently traded

# p.27, 79: Delta Concentration Thresholds for FX Risk
fx_delta_CT = {
    'Category1' : 8900, # Significantly material 
    'Category2' : 2000, # Frequently traded 
    'Others' : 250, # All other currencies
}

# p.27, 81: Vega Concentration Thresholds for IR Risk
ir_vega_CT = {
    'Others' : 93,   # All other currencies
    'USD'    : 2400, # Regular volatility, well-traded 
    'EUR'    : 2400, # Regular volatility, well-traded 
    'GBP'    : 2400, # Regular volatility, well-traded
    'AUD'    : 240,  # Regular volatility, less well-traded 
    'CAD'    : 240,  # Regular volatility, less well-traded 
    'CHF'    : 240,  # Regular volatility, less well-traded 
    'DKK'    : 240,  # Regular volatility, less well-traded 
    'HKD'    : 240,  # Regular volatility, less well-traded 
    'KRW'    : 240,  # Regular volatility, less well-traded 
    'NOK'    : 240,  # Regular volatility, less well-traded 
    'NZD'    : 240,  # Regular volatility, less well-traded 
    'SEK'    : 240,  # Regular volatility, less well-traded 
    'SGD'    : 240,  # Regular volatility, less well-traded 
    'TWD'    : 240,  # Regular volatility, less well-traded
    'JPY'    : 740,  # Low volatility
}

# p.27, 83: Vega Concentration Thresholds for Credit Spread Risk
credit_vega_CT = {
    "Qualifying" : 240, 
    "Non-Qualifying" : 56,
}

# p.28, 84: Vega Concentration Thresholds for Equity Risk
equity_vega_CT = {
    1 : 140,  # Emerging Markets  - Large Cap
    2 : 140,  # Emerging Markets  - Large Cap
    3 : 140,  # Emerging Markets  - Large Cap
    4 : 140,  # Emerging Markets  - Large Cap
    5 : 1600, # Developed Markets - Large Cap
    6 : 1600, # Developed Markets - Large Cap
    7 : 1600, # Developed Markets - Large Cap
    8 : 1600, # Developed Markets - Large Cap
    9 : 38,   # Emerging Markets  - Small Cap
    10: 240,  # Developed Markets - Small Cap
    11: 9800, # Indexes, Funds, ETFs, Volatility Indexes
    12: 9800, # Indexes, Funds, ETFs, Volatility Indexes
    0 : 38,   # Residual - Not classified
}

# p.28, 85: Vega Concentration Thresholds for Commodity Risk
commodity_vega_CT = {
    1 : 130,  # Coal
    2 : 1700, # Crude Oil
    3 : 290,  # Oil Fractions 
    4 : 290,  # Oil Fractions 
    5 : 290,  # Oil Fractions 
    6 : 2300, # Natural Gas 
    7 : 2300, # Natural Gas 
    8 : 800,  # Power 
    9 : 800,  # Power 
    10: 74,   # Freight, Dry or Wet 
    11: 420,  # Base metals 
    12: 700,  # Precious Metals 
    13: 560,  # Agricultural 
    14: 560,  # Agricultural 
    15: 560,  # Agricultural 
    16: 74,   # Other 
    17: 300,  # Indices 
}

# p.28, 86: Vega Concentration Thresholds for FX Risk
fx_vega_CT = {
    'Category1-Category1' : 3900,
    'Category1-Category2' : 1400,
    'Category1-Category3' : 640,
    'Category2-Category2' : 690,
    'Category2-Category3' : 440,
    'Category3-Category3' : 280,
}

# p.29, 88: Correlation between Risk Classes within Product Classes
corr_params = list(
    zip(
        [1.00 ,0.29 ,0.28 ,0.31 ,0.35 ,0.18],
        [0.29 ,1.00 ,0.51 ,0.61 ,0.43 ,0.35],
        [0.28 ,0.51 ,1.00 ,0.47 ,0.34 ,0.18],
        [0.31 ,0.61 ,0.47 ,1.00 ,0.47 ,0.30],
        [0.35 ,0.43 ,0.34 ,0.47 ,1.00 ,0.31],
        [0.18 ,0.35 ,0.18 ,0.30 ,0.31 ,1.00],
    )
)