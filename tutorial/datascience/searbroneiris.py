import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())


print(iris['species'].unique())

sns.pairplot(iris)
plt.show()

g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
plt.show()

tips = sns.load_dataset('tips')
print(tips)
g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.distplot, 'total_bill')
plt.show()

tips = sns.load_dataset('tips')
print(tips)
g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.scatterplot, 'total_bill', 'tip')
plt.show()

