import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())
print(flights.head())

tc= tips.corr()

print(tc)

sns.heatmap(tc, annot=True, cmap='coolwarm')
plt.show()

pt = flights.pivot_table(index='month', columns='year', values='passengers')
print(pt)

sns.heatmap(pt, linecolor='white', linewidths=1)
plt.show()

sns.clustermap(pt, cmap='coolwarm', standard_scale=1)
plt.show()
