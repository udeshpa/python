import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

print(cancer.keys())
print(cancer['DESCR'])

df_feats = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

from sklearn.model_selection import train_test_split

X = df_feats
y = cancer['target']

print(X.head())
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.svm import SVC

model = SVC()

model.fit(X_train, y_train)

print(f'{model.__dict__ }')

predictions = model.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, predictions))

print(confusion_matrix(y_test, predictions))

from sklearn.model_selection import GridSearchCV

param_grid = {
  'C': [0.1, 1, 10, 100, 1000],
  'gamma': [1, 0.1, 0.01, 0.001, 0.001]
}

grid = GridSearchCV(SVC(), param_grid, verbose=3)

grid.fit(X_train, y_train)

print(grid.best_params_, grid.best_estimator_)

grid_pred = grid.predict(X_test)

print(classification_report(y_test, grid_pred))

print(confusion_matrix(y_test, grid_pred))



