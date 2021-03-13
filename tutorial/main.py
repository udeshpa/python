# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import test.test1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def strings():
    message = 'Bobby\'s world'
    print(message)
    message = '''Bobby's world was a
      good cartoon movie'''
    print(message)


def string_methods():
    message = 'Hello, World'
    print(message[0:5])
    print(message.lower())
    print(message.upper())
    print(message.count('Hello'))
    print(message.count('l'))
    print(message.find('World'))
    print(message.find('Universe'))

    print(message.replace('World', 'Universe'))

    greeting = 'Hello'
    name = 'Michael'
    message = greeting + ', ' + name
    print(message)

    message = '{}, {}. Welcome!'.format(greeting, name)
    print(message)

    message = '{one}, {two}. Welcome!'.format(one=greeting, two=name)
    print(message)

    message = f'{greeting}, {name.upper()}. Welcome!'
    print(message)

    print(dir(name))
    print(help(str))
    print(help(str.lower))

def int_func():
    a = 3
    print(type(a))
    print("3/2 is : {} and 3//2 is {}, 3 ** 2 is {}, 3 % 2 is {}".format(3/2, 3//2, 3 ** 2, 3 % 2))
    print("3 * 2 + 1 is {}, abs(-3) is {}, round(3.7534434, 2) ".format(3 * 2 + 1, abs(-3)), round(3.7534434, 2))
    num_1 = '100'
    num_2 = '200'

    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #help(test)
    #test.test1.test_func()
    int_func()
    #strings()
    string_methods()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
