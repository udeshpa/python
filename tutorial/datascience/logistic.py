import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

train = pd.read_csv('titanic_train.csv')

print(train.head())
print(train.columns)

print(sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis'))

plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived', hue='Sex', data=train)

plt.show()

sns.countplot(x='Survived', hue='Pclass', data=train)

plt.show()


sns.displot(train['Age'].dropna(), kde=False, bins=30)
plt.show()

sns.countplot(x='SibSp', data=train)

plt.show()

train['Fare'].hist(bins=40)
plt.show()

sns.boxplot(x='Pclass', y='Age', data= train)
plt.show()

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]


    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis = 1)

sns.heatmap(train.isnull(), yticklabels=False, cbar=False)
plt.show()


train.drop('Cabin', axis=1, inplace=True)

train.dropna(inplace=True)

sex = pd.get_dummies(train['Sex'], drop_first=True)
embark = pd.get_dummies(train['Embarked'], drop_first=True)

pd.concat([train, sex, embark], axis=1)

train.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)

print(train.head())

X=train.drop('Survived', axis=1)
y=train['Survived']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()

logmodel.fit(X_train, y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, predictions))
