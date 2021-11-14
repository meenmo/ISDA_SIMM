import pandas as pd
import agg_margins

def main(calc_currency='USD',exchange_rate=1):

    path = '../CRIF/'
    crif = pd.read_csv(path+'crif.csv', header=0)
    calc = agg_margins.AggregateMargins(crif,calc_currency,exchange_rate)
    results = calc.simm()
    print(results)
    # df.to_excel('...')

if __name__ == '__main__':
    main('USD')
