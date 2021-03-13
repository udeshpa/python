if True:
    print('Conditional was true')
else:
    print('Conditional was false')

language = 'Python'

if language == 'Python':
    print('language is Python')
elif language == 'Java':
    print('language is Java')
else:
    print('No match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')

if not logged_in:
    print('Not logged in')

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(f'{a == b} and {a is b}')

#False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence, e.g. '', [], ()
# Any empty mapping, e.g {}

a = [False, None, 0, 0.0, '', [], (), {}]

for condition in a:
    if condition:
        print('Condition was true')
    else:
        print('Condition was false')
