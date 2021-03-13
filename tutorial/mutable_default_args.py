
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)


emps = ['john' , 'jane']


add_employee('Jack', emps)
add_employee('Tim', emps)


#Default argument are evaluated once when the function is created. It is not creating a new empty list everytime
# the function is executed. Mutable types like list it is created once.
add_employee('Tom')
add_employee('Mary')
add_employee('Ann')


def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []

    emp_list.append(emp)
    print(emp_list)


add_employee('Tom')
add_employee('Mary')
add_employee('Ann')

import time
from datetime import datetime


def display_time(time=datetime.now()):
    print(time.strftime('%B %d, %Y %H: %M: %S'))


display_time()
time.sleep(1)
display_time()


def display_time(time=None):
    if time is None:
        time = datetime.now()

    print(time.strftime('%B %d, %Y %H: %M: %S'))

display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
