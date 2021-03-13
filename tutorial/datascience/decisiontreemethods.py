import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('kyphosis.csv')

print(df.columns)
print(df.head())

sns.pairplot(df, hue='Kyphosis')
plt.show()

from sklearn.model_selection import train_test_split

X = df.drop('Kyphosis', axis=1)
y = df['Kyphosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()

dtree.fit(X_train, y_train)

predictions = dtree.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, predictions))

print(classification_report(y_test, predictions))


from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
rfc_preds = rfc.predict(X_test)

print(confusion_matrix(y_test, rfc_preds))

print(classification_report(y_test, rfc_preds))
