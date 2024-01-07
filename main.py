import pandas as pd
from src.agg_margins import SIMM


if __name__ == '__main__':

    path = 'CRIF/'
    crif = pd.read_csv(path+'crif.csv', header=0)
    portfolio1 = SIMM(crif, "USD", 1)
    
    # Total SIMM
    print(portfolio1.simm)

    # SIMM Break Down
    print(portfolio1.simm_break_down)
    
