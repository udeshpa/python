li = [9, 1, 6, 8, 4, 7,2]

s_li = sorted(li, reverse=True) # returns a new sorted list

print(f'Sorted {s_li} original {li}')

li.sort(reverse=False)

print(f'Sorted original {li}') # returns None, sorts original list

tup = (9, 1, 6, 8, 4, 7,2)
s_tup = sorted(tup)

print(s_tup)

di = { 'name' : 'Uday', 'job' : 'programmer', 'age' : None, 'os' : 'Mac'}

s_di = sorted(di)

print(s_di)

li = [-6, -5, -4, 1, 2, 3]

s_li = sorted(li, key=abs)
print(s_li)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, {self.salary})'


e1 = Employee('Carl', 29, 50000)
e2 = Employee('Dave', 42, 70000)
e3 = Employee('John', 39, 80000)
employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort, reverse=True)


print(s_employees)

s_employees = sorted(employees, key=lambda e: e.name, reverse=True)
print(s_employees)

from operator import attrgetter

s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)
