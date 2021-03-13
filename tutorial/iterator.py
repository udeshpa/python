nums = [1,2,3]

i_nums = nums.__iter__()

#i_nums = iter(nums) Same as __iter__()

print(dir(nums))

print(i_nums)
print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
#print(next(i_nums))

i_nums = iter(nums)
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)


for num in nums:
    print(num)

nums = MyRange(1, 10)
print(next(nums))
print(next(nums))


#Generators are also iterators
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(6, 10)
print(next(nums))
print(next(nums))

for num in nums:
    print(num)

#A generator that goes on indefinitely


def my_range(start):
    current = start
    while True:
        yield current
        current += 1

