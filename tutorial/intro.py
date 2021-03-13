#import my_module
#import my_module as mm
from my_module import find_index as fi, test

import sys
import random
#import math
import datetime
import calendar

courses = ['History', 'Art', 'Design']

#index = my_module.find_index(courses, 'History')

#index = mm.find_index(courses, 'History')

index = fi(courses, 'Design')
print(f'{index} is the index of Design')
print(test)
print(sys.path)
#sys.path.append()

random_course = random.choice(courses)

print(random_course)

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

import os

print(os.getcwd())
print(os.__file__)

import antigravity
