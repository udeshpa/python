import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('911.csv')

print(df.head())
print(df.info())

print(df.groupby('zip').count())

byzip = df.groupby('zip')
print(byzip.count().sort_values(by='lat',ascending=False))

bytwp = df.groupby('twp')
print(bytwp.count().sort_values(by='lat',ascending=False))

print(len(df['title'].unique()))

titles = df['title'].apply(lambda x:  x.split(":"))

print(titles, type(titles))
