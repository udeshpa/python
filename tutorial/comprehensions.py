nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []

for n in nums:
    my_list.append(n)

print(my_list)

my_list = [ n for n in nums]

print(my_list)

my_list = []
for n in nums:
    my_list.append(n * n)

print(my_list)

my_list = [n * n for n in nums]
print(my_list)

my_list = map(lambda n: n * n, nums)
print(list(my_list))

my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)

print(list(my_list))

my_list = [ n for n in nums if n % 2 == 0]

print(list(my_list))

my_list = filter(lambda n: n % 2 == 0, nums)
print(list(my_list))

my_list = []
for n in 'abcd':
    for m in range(4):
        my_list.append((n, m))
print(list(my_list))

my_list = [(n, m) for n in 'abcd' for m in range(4)]
print(list(my_list))

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = [ 'Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero

print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

my_tup = tuple(n for n in nums)
print(my_tup)


def gen_func(nums):
    for n in nums:
        yield n * n


g = gen_func(nums)
print(list(g))

