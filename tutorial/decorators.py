from functools import wraps


def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print(f'wrapper executed this function:{original_func.__name__}')
        return original_func(*args, **kwargs)
    return wrapper_func


def display():
    print('display function ran')


@decorator_func
def display2():
    print('display2 function ran')


decorated_display = decorator_func(display)
decorated_display()

display2()


@decorator_func
def display_info(name, age):
    print(f'display ran with arguments ({name} {age})')


display_info('john', 25)


class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(f'call method executed this function:{self.original_func.__name__}')
        return self.original_func(*args, **kwargs)


@decorator_class
def display_info_2(name, age):
    print(f'display_info_2 ran with arguments ({name} {age})')


display_info_2('john', 25)


def my_logger(orig_func):
    import logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args} and kwargs {kwargs}')
        orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, *kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in : {t2} sec')
        return result

    return wrapper


@my_logger
def display_info_3(name, age):
    print(f'display_info_3 ran with arguments ({name} {age})')


display_info_3('hank', 30)

import time


@my_timer
@my_logger
def display_info_4(name, age):
    time.sleep(1)
    print(f'display_info_4 ran with arguments ({name} {age})')


display_info_4('tom', 45)

#decorator with arguments
def prefix_decorator(prefix):
    def decorator_func_with_args(original_func):
        def wrapper_func(*args, **kwargs):
            print(f'{prefix} wrapper executed this function:{original_func.__name__}')
            return original_func(*args, **kwargs)

        return wrapper_func
    return decorator_func_with_args;


@prefix_decorator('Testing:')
def display5():
    print('display5 function ran')


display5()
