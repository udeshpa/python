import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('kc_house_data.csv')

print(df.head())

print(df.isnull().sum())

print(df.describe().transpose())

plt.figure(figsize=(10,6))
sns.distplot(df['price'])

plt.show()

sns.countplot(df['bedrooms'])

plt.show()

print(df.corr()['price'])

sns.scatterplot(x='price', y='sqft_living', data=df)

plt.show()

plt.figure(figsize=(10,6))

sns.boxplot(x='bedrooms', y='price', data=df)

plt.show()
