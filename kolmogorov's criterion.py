from scipy import stats
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('Throws_socks_in_the_bin.csv')

df['throws'].plot(kind='bar')
df1 = pd.DataFrame(data={
    'df_strikes': df['throws']})


df1.plot.kde()
plt.show()

print(stats.kstest(df1['df_strikes'], 'norm', (df1['df_strikes'].mean(), df1['df_strikes'].std()), N=len(df1['df_strikes'])))
print(stats.kstest('norm', 'norm', N=500))
#print(df)
"""pvalue is too small, K-S is relatively big, so hypothesis has not been approved"""
