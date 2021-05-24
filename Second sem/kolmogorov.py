from scipy import stats
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('Resistance')


df.resists.plot.kde()
plt.show()

print(stats.kstest(df['resists'], 'norm', (df['resists'].mean(), df['resists'].std()), N=len(df['resists'])))
print(stats.kstest('norm', 'norm', N=500))
#print(df)
#гипотеза подтвердилась
