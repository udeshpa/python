import itertools

counter = itertools.count(start=5, step=5)
print(next(counter))
print(next(counter))

counter = itertools.count(start=5, step=-2.5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data)) #zip ends on shorter iterable

print(daily_data)

daily_data = list(itertools.zip_longest(range(10), data)) #zip ends on shorter iterable

print(daily_data)

counter = itertools.cycle([1, 2, 3])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.cycle(('ON', 'OFF'))

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.repeat(2, times=3)

print(next(counter))
print(next(counter))
print(next(counter))
#print(next(counter)) this will generate stopiteration exception

cubes = list(map(pow, range(10), itertools.repeat(3)))
print(cubes)

cubes = list(itertools.starmap(pow, [(0,3), (1,3), (2,3), (3,3)]))
print(cubes)

letters = ['a', 'b', 'c', 'd']

numbers = [1, 2, 3, 2, 1, 0]
names = ['Uday', 'Ishan']

result = itertools.combinations(letters, 3)
for item in result:
    print(item)

result = itertools.permutations(letters, 2)
for item in result:
    print(item)

result = itertools.product(numbers, repeat=4) #gives cartesian product where repeats are allowed
for item in result:
    print(item)

result = itertools.combinations_with_replacement(numbers, 2)
for item in result:
    print(item)

combined = letters + numbers + names
print(combined)

combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)

result = itertools.islice(range(10), 5)
for item in result:
    print(item)

result = itertools.islice(range(10), 1, 6)
for item in result:
    print(item)

result = itertools.islice(range(10), 1, 6, 2)
for item in result:
    print(item)

with open('test.log', 'r') as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end='')

selectors = [True, True, False, True]
result = itertools.compress(letters, selectors) #equivalent to builtin filter function except that filter uses function

for item in result:
    print(item)


def lt_2(n):
    if n < 2:
        return True
    return False


result = filter(lt_2, numbers)

for item in result:
    print(item)

result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)

result = itertools.dropwhile(lt_2, numbers)
for item in result:
    print(item)

result = itertools.takewhile(lt_2, numbers)
for item in result:
    print(item)

result = itertools.accumulate(numbers) #keeps a running total as the iteration continues
for item in result:
    print(item)

import operator

result = itertools.accumulate(numbers, operator.mul) #keeps a running product as the iteration continues
for item in result:
    print(item)

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


def get_state(person):
    return person['state']

print(get_state({
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }))

person_group = itertools.groupby(people, get_state) #assumes that the input is already sorted by the key
for key, group in person_group:
    print(key, group)
    for person in group:
        print(person)

person_group = itertools.groupby(people, get_state)
copy1, copy2 = itertools.tee(person_group)

for i in copy1:
    print(i)
