import numpy as np

my_list = [1,2, 3]

arr = np.array(my_list)
print(arr)
my_mat = [[1,2,3], [4,5,6], [7,8,9]]

arr = np.array(my_mat)

print(arr)

arr = np.arange(0,11, 2)
print(arr)

#reshape the array in 3 rows and 2 columns
arr = arr.reshape(3,2)
print(arr)

arr = np.zeros((2,3))

print(arr)

arr = np.ones((2,3))

print(arr)

#10 evenly spaced points between 0 and 5
arr = np.linspace(0,5, 10)

print(arr)

print(np.eye(4))

#array of uniformly distributed random numbers between 0 and 1
print(np.random.rand(5))

#two dimensional array of uniformly distributed random numbers between 0 and 1
print(np.random.rand(5, 5))

#array of nomrally (gaussian) distributed random numbers
print(np.random.randn(4,4))

#10 random int between 1 to 100, lowest inclusive and highest exclusive
print(np.random.randint(1,100, 10))

arr = np.random.rand(5)
#max and min of array and their index locations
print(f'{arr} and {arr.max()} and {arr.min()} and {arr.argmax()} and {arr.argmin()} and {arr.shape} and {arr.dtype}')

#brodcast the number 100 to elements in array
arr[0:2] = 100
print(arr)


arr =  np.arange(0, 100)
print(arr)

slice_of_array  = arr[0:20]
print(slice_of_array)

#changing/broadcasting to the main array changes the main array
slice_of_array[0:20] = 90
print(f'{arr}')

#makes an identical copy of the array
copy_arr = arr.copy()

arr_2d = np.array([[5, 10,15],[25,30,35],[35,40,45]])
print(arr_2d)


print(f'{arr_2d[0][0]} and {arr_2d[0]}')

print(f'{arr_2d[2, 1]}')

#Grabbing submatrices every thing upto and excluding row 2 and everything after and including column 1
print(f'{arr_2d[:2, 1:]}')


arr =  np.arange(0, 100)
#comparison generates an array of booleans for each element
bool_ary = arr > 55
print(f'{bool_ary}')

#creates a sub array from arr where boolary is true
print(arr[bool_ary])


print(arr[arr < 50])

arr = np.arange(1, 11)

print(arr + arr)

print(arr - arr)


print(arr + 100, arr - 20)

print(arr * arr)

print(f'{arr / arr}')

print(f'{1 / arr}')



print(f'{arr ** 3} and {np.sqrt(arr)} and {np.exp(arr)} and {np.max(arr)}')

print(f'{np.log(arr)} and {np.sin(arr)}')

