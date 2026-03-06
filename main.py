import argparse
import pandas as pd
from src.agg_margins import SIMM


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='CRIF/crif.csv')
    args = parser.parse_args()

    crif = pd.read_csv(args.file, header=0)
    portfolio1 = SIMM(crif, "USD", 1)
    
    # Total SIMM
    print(portfolio1.simm)

    # SIMM Break Down
    print(portfolio1.simm_break_down)
    
