courses = ['History', 'Maths', 'Comp. Sci', 'Physics']

print(len(courses))

print(courses[0:2])
print(courses[3:])

courses.append('Art')
courses.insert(0, 'Art')

courses_2 = ['Art', 'Education']

courses.extend(courses_2)

courses.remove('Maths')

print(courses)

print(courses.pop())

print(courses)
courses.reverse()

print(courses)

courses.sort(reverse=True)

print(courses)

sorted_courses = sorted(courses)
print(sorted(sorted_courses))

int_list = [3,5,8]
print("{}, {}, {}".format(min(int_list), max(int_list), sum(int_list)))

print(f"{courses.index('Physics')}, {courses[0]}")

print('Art' in courses)

for item in courses:
    print(item)

for index, course in enumerate(courses, start=1):
    print(f"{course}:{index}")

course_str = ' - '.join(courses)

print(course_str)
new_list = course_str.split((' - '))
print(new_list)


courses_2 = courses
print(courses)
print(courses_2)
courses[0] = 'Engineering'
print(courses)
print(courses_2)

tuple_1 = ('Physics', 'History', 'Comp. Sci', 'Art', 'Art', 'Art')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art' Errror tuples are immutable

set1 = {'Physics', 'History', 'Comp. Sci', 'Art', 'Art', 'Art'} # unique elements and unordered

print(set1)
print('Physics' in set1)

set2 = {'Physics', 'History', 'Comp. Sci', 'Architecture'}
set3 = {'Physics', 'History', 'Math', 'Art'}

print(set2.intersection(set3))
print(set3.difference(set2))
print(set3.union(set2))

# Empty Lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty set
# empty_set = {} //This does not work. Creates dictionary
empty_set = set()


# Dictionaries
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'History']}
print(student['name'], student['courses'])

print(student.get('phone', 'Not Found'))

student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student.get('phone', 'Not Found'), student['name'])

student.update({'name': 'Jim', 'age': 26})
print(student)

del student['age']
print(student)

phone = student.pop('phone')
print(student)

print(len(student), student.keys(), student.values(), student.items())  # items returns name value tuples

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
