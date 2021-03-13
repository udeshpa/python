#First class Functions

def square(x):
    return x * x


f = square
print(f)
print(f(5))

#pass a function as argument


def my_map(func, arg_list):
    result = []
    for arg in arg_list:
        result.append(func(arg))

    return result


r = my_map(square, [1, 2, 3, 4, 5])

print(r)
print(my_map(lambda n: n*n*n, [1, 2, 3, 4, 5]))


def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message

log_hi = logger('hello')
log_hi()
logger('hello')()

def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text

html_tag('h1')('some message')

#closures
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func


my_func = outer_func()

print(my_func.__name__)

#A closure is an inner function that has access to local variable in its scope when it was created even if the outer
#function has exited.

my_func()


def outer_func_2(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func_2('Hi')
hello_func = outer_func_2('Hello')

# A closure closes over the free variables from their environment
hi_func()
hello_func()


import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(f'Running {func.__name__} with arguments {args}')
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x,y):
    return x-y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(4,5)
add_logger(10,6)
sub_logger(10, 5)
sub_logger(11, 7)
