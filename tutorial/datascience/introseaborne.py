import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')

print(tips.head())

#kerenel density estimation, bins is number of buckets
sns.displot(tips['total_bill'], kde=True, bins=20)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
plt.show()

sns.pairplot(tips, hue='sex', palette='coolwarm')
plt.show()

sns.rugplot(tips['total_bill'])
plt.show()

sns.kdeplot(tips['total_bill'])
plt.show()

#Categorical plots
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
plt.show()

sns.countplot(x='sex', data=tips)
plt.show()

sns.boxplot(x='day',y='total_bill', data=tips, hue='smoker')
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips)
plt.show()

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', dodge=True)
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')
plt.show()

sns.factorplot(x='day', y='total_bill', data=tips, kind='violin')
plt.show()

sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
plt.show()

sns.set_style('whitegrid')
sns.set_context('poster', font_scale=3)
#plt.figure(figsize=(12,3))
sns.countplot(x='sex', data=tips)
plt.show()
