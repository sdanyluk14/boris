#%%
import pandas as pd
import matplotlib.pyplot as plt
import functions

plt.style.use('dark_background')

c23 = pd.read_csv (r'chelsea_history_aggregate/chelsea_matches_22_23.txt')
c23 = c23.loc[~c23['xG'].isnull()]
c23['xDf'] = c23['xG'] - c23['xGA']

print(c23.columns)


print(functions.create_lookback_df(c23, ['xG', 'GF', 'xGA', 'GA'], 10))
print(functions.rolling_avg(c23, 'xG'))

dfo = functions.create_lookback_df(c23.loc[c['Comp'] == 'Premier League'].reset_index(), 
                                ['xG', 'GF', 'xGA', 'GA', 'xDf'], 10)
dfo['Date'] = c23['Date'][10:]

#%%
print(dfo.index())

plt.plot(dfo['xG'], color = 'green')
plt.scatter(dfo['xG'], color = 'green')
plt.plot(dfo['xGA'], color = 'red')
plt.scatter(dfo['xGA'], color = 'red')
plt.show()

plt.plot(dfo['xDf'], color = 'green')
plt.show()

# %%
prem = c.loc[c['Comp'] == 'Premier League'].reset_index()
print(prem.columns)
plt.plot(prem['Date'], prem['xDf'])
plt.xticks(rotation=90)



# %%