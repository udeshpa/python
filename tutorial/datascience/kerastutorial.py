import pandas as pd
import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv('fake_reg.csv')

print(df.head())

sns.pairplot(df)

plt.show()



from sklearn.model_selection import train_test_split

X = df[['feature1', 'feature2']].values

print(X)

y = df['price'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.preprocessing import MinMaxScaler

scalar = MinMaxScaler()
scalar.fit(X_train)
X_train = scalar.transform(X_train)
X_test = scalar.transform(X_test)

print(X_train, X_train.max(), X_train.min())

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

#model = Sequential([Dense(units=4, activation='relu'), Dense(2, activation='relu'), Dense(1)])

model = Sequential()
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1))


#mean square error mse
model.compile(optimizer='rmsprop', loss='mse')
model.fit(x=X_train, y=y_train, epochs=250)


print(model.history.history)

lossdf = pd.DataFrame(model.history.history)

lossdf.plot()

plt.show()

print(model.evaluate(X_train, y_train))
print(model.evaluate(X_test, y_test))

test_predictions = model.predict(X_test)
test_predictions = pd.Series(test_predictions.reshape(300,))
pred_df = pd.DataFrame(y_test, columns=['Test True Y'])

pred_df = pd.concat([pred_df, test_predictions], axis=1)
pred_df.columns=['Test True Y', 'Model Predictions']
print(pred_df)

sns.scatterplot(x='Test True Y', y='Model Predictions', data=pred_df)
plt.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error
print(mean_absolute_error(pred_df['Test True Y'], pred_df['Model Predictions']))
print(mean_squared_error(pred_df['Test True Y'], pred_df['Model Predictions']))

print(df.describe())

new_gem = [[998, 1000]]

new_gem = scalar.transform(new_gem)
print(model.predict(new_gem))

from tensorflow.keras.models import load_model

model.save('my_gem_model.h5')

later_model = load_model('my_gem_model.h5')

print(later_model.predict(new_gem))




