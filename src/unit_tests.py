import pandas as pd
import agg_margins

from pdb import set_trace as bp

if __name__ == '__main__':

    path = 'CRIF/'
    df_sensitivity_inputs = pd.read_excel(
        path+'ISDA-SIMM-UnitTesting-v2.5.xlsx', 
        sheet_name="Sensitivity Inputs", 
        skiprows=20
    ).dropna(
        how='all' # Drop rows with all NaN values
    )
    
    # Drop rows of the header
    df_sensitivity_inputs = df_sensitivity_inputs[df_sensitivity_inputs.ne(df_sensitivity_inputs.columns).any(axis=1)]

    df_combinations_10day = pd.read_excel(
        path+'ISDA-SIMM-UnitTesting-v2.5.xlsx', 
        sheet_name="Combinations (10-day)"
    )

    # for i, row in df_combinations_10day[334:].iterrows():
    for i, row in df_combinations_10day[329:].iterrows():
        ids = row["Sensitivity Ids"].split(",")
        if "All " in ids[0]:
            ids = [id.replace("All ", "")+"_" for id in ids]
            crif = pd.DataFrame()
            for id in ids:
                crif = pd.concat([crif, df_sensitivity_inputs[df_sensitivity_inputs["Sensitivity_Id"].str.startswith(id)]])      
        else:
            crif = pd.DataFrame()
            for id in ids:
                crif = pd.concat([crif, df_sensitivity_inputs[df_sensitivity_inputs["Sensitivity_Id"]==id]])

        unit_test = agg_margins.AggregateMargins(crif,"USD", 1)
        simm_bm = row["SIMM Benchmark"]

        # print(crif)
        if abs(unit_test.simm - simm_bm) > 0.01:
            bp()
        print(row["Combination Id"])
        #     print(row["Combination Id"]+"@")
        # else:


