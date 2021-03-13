import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']

my_data = [10, 20, 30]

arr = np.array(my_data)

d ={'a': 10, 'b': 20, 'c': 30}


print(f'With list {pd.Series(data=my_data)}')

print(pd.Series(data=my_data, index=labels))

#works with numpy arrays too
print(pd.Series(data=arr, index=labels))

#works with dictionary
print(pd.Series(d))

print(pd.Series(data=labels))

print(pd.Series(data=[sum, print, len]))

ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])

print(ser1)

print(ser1['USA'])

ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])

print(ser2)


#adding two Series objects, fills NaN for null values
print(ser1 + ser2)
