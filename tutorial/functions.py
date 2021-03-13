def hello_func(greeting, name="you"):
    return '{}, {} '.format(greeting, name)

print(hello_func)
print(hello_func('Hi'))
print(hello_func('Hi', 'John'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}


student_info(*courses, ** info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """ Return True for leap year """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """ Return number of days in a month """

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2017, 2))
print(days_in_month(2016, 2))
print(days_in_month(2000, 2))
