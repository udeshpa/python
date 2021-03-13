import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)

print(df['W'], type(df['W']))

print(df[['W', 'Z']], type(df[['W', 'Z']]))

df['new'] = df['W'] + df['Y']

print(df)

#drop a columns, need to select axis, It drops in place

print(df.drop('new', axis=1))

#original still has the column 'new'
print(df)

df.drop('new', axis=1, inplace=True)

print(df)

#dropping rows
df.drop('E', axis=0, inplace=True)


print(df, df.shape)

#selecting rows
print(df.loc['A'])
print(df.iloc[2])

print(df.loc['B', 'Y'])
print(df.loc[['A', 'B'], ['W', 'Y']])

print(df > 0)

booldf = df > 0

print(df[booldf])

print(df[df > 0])

print(df['W'] > 0)

print(df[df['W'] > 0])

print(df[df['W'] > 0]['X'])
print(df[df['W'] > 0][['X', 'Y']])


print(df[(df['W'] > 0) & (df['Y'] > 0)][['X', 'Y']])

print(df[(df['W'] > 0) | (df['Y'] > 0)][['X', 'Y']])

print(df.reset_index(inplace=False))

newind = 'CA NY WY OR '.split()

df['States'] = newind

print(df)

df.set_index('States', inplace=True)

print(df)



outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']

inside = [1,2,3,1,2,3]

hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

df = pd.DataFrame(randn(6,2), hier_index, ['A', 'B'])

print(df)

print(df.loc['G1'])

print(df.loc['G1'].loc[1])

df.index.names = ['Groups', 'Num']

print(df)

print(df.loc['G2'].loc[2]['B'])

#To grab a cross section

print(df.xs(1, level='Num'))

d = {'A': [1,2,np.nan], 'B':[5, np.nan, np.nan], 'C': [1,2,3]}
df = pd.DataFrame(d)
print(df)

print(df.dropna(axis=0))

print(df.dropna(axis=0, thresh=2))

print(df.fillna(value='Fill Value'))
print(df.fillna(value=df['A'].mean))

data = {
  'Company' : ['Goog', 'Goog', 'MSFT', 'MSFT', 'FB', 'FB'],
  'Person': ['Sam', 'Charlie', 'Amy', 'Venessa', 'Carl', 'Sarah'],
  'Sales': [200, 120, 340,124, 243, 350]
}


df = pd.DataFrame(data)

print(df)

bycompany = df.groupby('Company')
print(bycompany.mean(), type(bycompany))
print(bycompany.sum())
print(bycompany.std())

print(bycompany.sum().loc['FB'])

print(df.groupby('Company').count())

print(df.groupby('Company').max())
print(df.groupby('Company').describe())

print(df.groupby('Company').describe().transpose())

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    }, index = [0, 1, 2, 3]
)
df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7'],
    }, index = [4, 5, 6, 7]
)

df3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11'],
    }, index = [8, 9, 10, 11]
)

print(f'{df1} \n {df2} \n {df3}')

print(pd.concat([df1, df2, df3]))
print(pd.concat([df1, df2, df3], axis=1))

left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})


right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

print(f'{left} \n {right}')

merged = pd.merge(left, right, how='inner', on='key')

print(f'{merged}')

left = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})


right = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

print(f'{left} \n {right}')

merged = pd.merge(left, right,  on=['key1', 'key2'])

print(f'{merged}')


print(f'{left} \n {right}')

merged = pd.merge(left, right,  how= 'outer', on=['key1', 'key2'])

print(f'{merged}')

left = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
},
    index=['K0', 'K1', 'K2']
)


right = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
},
  index=['K0', 'K2', 'K3']
)

#join on index keys
print(f'{left} \n {right}')

joined = left.join(right,  how='inner')

print(f'{joined}')

joined = left.join(right,  how='outer')

print(f'{joined}')

df = pd.DataFrame({

  'col1': [1,2,3,4],
  'col2': [444,555,666,444],
  'col3': ['abc', 'def', 'ghi', 'xyz']
})

print(df.head())

print(f'{df["col2"].unique()} \n {df["col2"].nunique()} \n {df["col2"].value_counts()}')

print(f'{df[(df["col1"] > 2 ) & (df["col2"] == 444)]}')

def times2(x) :
  return x * 2


out = df['col1'].apply(times2)

print(f'\n{df}, \n {out}')

out = df['col1'].apply(lambda x : x * 2)

print(f'\n{df}, \n {out} \n {df.columns}')

df.drop('col1', axis=1, inplace=True)
print(f'\n{df}')

print(f'{df.sort_values(by="col2")} \n {df.isnull()}')

df = pd.DataFrame({
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': ['x', 'y', 'x', 'y', 'x', 'y'],
    'D': [1, 3, 2, 5, 4, 1]
})

pt = df.pivot_table(values='D', index=['A', 'B'], columns=['C'])

print(f'{df} \n  {pt}')

df = pd.read_csv('example')

print(df)


#index should be false for exact cloning. otherwise the new file will include the default index of the data frame
df.to_csv('my_output', index=False)
# pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')

data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')

print(f'{data[0]} \n {data[0].columns}')

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con=engine)

print(sqldf)
