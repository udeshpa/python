import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('USA_Housing.csv')

print(df.head())
print(df.columns)
print(df.info())

sns.pairplot(df)
plt.show()

sns.distplot(df['Price'])
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.show()

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

y = df['Price']


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, y_train)

print(lm.intercept_)

print(lm.coef_)


cdf =   pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])

print(cdf)

#Sample real boston housing data

from sklearn.datasets import load_boston

boston = load_boston()

print(boston)

print(boston['DESCR'])

#Actaul feature data
print(boston['data'])

#names of features
print(boston['feature_names'])

#output/house prices
print(boston['target'])

predictions = lm.predict(X_test)

print(predictions)


plt.scatter(y_test, predictions)

plt.show()

sns.distplot((y_test-predictions))

plt.show()


from sklearn import  metrics

print(metrics.mean_absolute_error(y_test, predictions))

print(metrics.mean_squared_error(y_test, predictions))

print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
