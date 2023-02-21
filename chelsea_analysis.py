#%%
import pandas as pd
import matplotlib.pyplot as plt
import functions

c = pd.read_csv (r'chelsea_matches_22_23.txt')

print(c.columns)


def rolling_avg(df, col) -> float:
    return df[col].mean()

print(c.iloc[:5])
print(c.columns)


print(create_lookback_df(c, ['xG', 'GF', 'xGA', 'GA'], 10))
print(rolling_avg(c, 'xG'))

dfo = create_lookback_df(c, ['xG', 'GF', 'xGA', 'GA'], 10)

#%%
plt.plot(dfo['xG'])
plt.plot(dfo['xGA'])
plt.show()
# %%
