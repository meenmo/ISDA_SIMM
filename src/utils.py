import math
from . import simm_tenor_list

# Calculate Concentration Threshold
def concentration_threshold(sum_s,T):
    return float(max(1, math.sqrt(abs(sum_s)/T)))

# Sum Sensitivities(AmountUSD) from CRIF
def sum_sensitivities(crif):
    return crif['AmountUSD'].sum()

# Extract tenors as a list from CRIF
def tenor_list(crif):
    label_1 = crif['Label1'].tolist()
    return list(set([x.lower() for x in label_1 if x.lower() in simm_tenor_list]))

# Extract distict values only from a list or a pandas column
def unique_list(x, column=None):
    if isinstance(x, list):
        seen = set()
        return [y for y in x if not (y in seen or seen.add(y))]
    else:
        # pandas.dataframe
        return x[column].unique().tolist()

# Extract currency pairs from CRIF as a list
def currencyPair_list(crif):
    currencyPair = [x for x in list(crif['Qualifier']) if (str(x) != 'nan' and len(str(x)) == 6)]
    currencyPair_list = []

    # Prevent from containing duplicates
    # e.g. KRWUSD is considered to be indentical with USDKRW
    for pair in currencyPair:
        if pair[3:]+pair[:3] not in currencyPair_list:
            currencyPair_list.append(pair)

    return list(set(currencyPair_list))

# Extract product classes from CRIF
def product_list(crif):
    product_list = [x for x in list(crif['ProductClass']) if (str(x) != 'nan')]
    return list(set(product_list))     

# Extract buckets from CRIF
def bucket_list(df):
    if 'Residual' in list(df['Bucket']):
        # Residual goes to 0
        bucket_list = [int(x) for x in list(df['Bucket']) if (str(x) != 'nan' and x != 'Residual' and x != 'Residual')]
        bucket_list.append(0)

    else:
        bucket_list = [int(x) for x in list(df['Bucket']) if str(x) != 'nan']
    
    return list(set(bucket_list))

# Scaling Function of time t (for Curvature Margin)
def scaling_func(t):
    t = t.lower()
    if t == '2w':
        return 0.5
    elif 'm' in t:
        t = (365/12) * float(t.replace('m', ''))
        return 0.5 * min(1, 14/t)
    elif 'y' in t:
        t = 365 * float(t.replace('y', ''))
        return 0.5 * min(1, 14/t)
