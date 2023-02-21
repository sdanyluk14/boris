# Helper functions for soccer analysis
import pandas as pd

def rolling_avg(df, col) -> float:
    return df[col].mean()

def create_lookback_df(df, cols, length):
    """
    Lookback function creates a rolling dataframe of results
    """
    df_output = pd.DataFrame(columns=cols, index = range(length, df.shape[0]))

    for i in cols:
        print(i)
        for j in range(length, len(df[i])):
            temp_out = rolling_avg(df.iloc[j-length: j], i)
            df_output.loc[j, i] = temp_out
    
    return(df_output)