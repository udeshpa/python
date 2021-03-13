import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('df1', index_col=0)
print(df1.head())

df2 = pd.read_csv('df2')
print(df2.head())


df1['A'].hist()
plt.show()

df1['A'].plot(kind='hist', bins=30)
plt.show()

df1['A'].plot.hist()
plt.show()

df2.plot.area(alpha=0.4)
print(df2.index)

plt.show()

df2.plot.bar(stacked=True)
plt.show()

df1.plot.line( y='B', use_index=True, figsize=(12,3), lw=1)
plt.show()

#set color based on another columns
df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')
plt.show()

#set size based on another columns
df1.plot.scatter(x='A', y='B', s=df1['C'] * 100)
plt.show()

df = pd.DataFrame(np.random.randn(1000,2), columns=['a','b'])
df.plot.hexbin(x='a', y='b', gridsize=25, cmap='coolwarm')
plt.show()

df2['a'].plot.kde()
plt.show()

df2['a'].plot.density()
plt.show()
