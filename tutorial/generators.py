def square_numbers(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return result


def square_numbers_gen(nums):
    for num in nums:
        yield num * num


my_nums = [1, 2, 3, 4, 5]

print(square_numbers(my_nums))

my_nums_gen = square_numbers_gen(my_nums)

#print(next(my_nums_gen))
#print(next(my_nums_gen))
#print(next(my_nums_gen))
#print(next(my_nums_gen))

for num in my_nums_gen:
    print(num)

my_nums_1 = [x * x for x in [1, 2, 3, 4, 5] ] #list comprehension
print(my_nums_1)

my_nums_2= (x * x for x in [1, 2, 3, 4, 5]) #generator for tthe above list comprehension
print(my_nums_2)

#converting generator to list

print(list(my_nums_2))
