import seaborn as sns
import matplotlib.pyplot as plt

#lmplot is linear model plot
tips = sns.load_dataset('tips')

print(tips.head())

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], scatter_kws={'s' : 100})
plt.show()

sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time')
plt.show()

sns.lmplot(x='total_bill', y='tip', data=tips, col='day',  hue='sex', aspect=0.6, height=8)
plt.show()
