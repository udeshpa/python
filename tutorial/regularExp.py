import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

print(r'\tTab')

pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])

pattern = re.compile(r'coreyms\.com') #backslash the dot is for the regex. The string is a raw string

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

pattern = re.compile(r'.') #matches every character but a new line charater
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#\d digits
#\D Not a digit
#\w word character (a-z, A-Z, 0-9, _)
#\W Not a word character
#\s whitespaces (space, tab,newline)
#\S not a whitespace
#\b word boundary
#\B Not a word boundary
#^ Beginning of a string
#$ End of String

pattern = re.compile(r'\bHa') #matches word boundry before Ha
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'^Start') #matches word boundry before Ha
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

pattern = re.compile(r'end$') #matches word boundry before Ha
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') #matches word boundry before Ha
matches = pattern.finditer(text_to_search )

for match in matches:
    print(match)

with open('data.txt', 'r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)

pattern = re.compile(r'[89]00.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search )

for match in matches:
    print(match)

pattern = re.compile(r'[^a-zA-Z]')
matches = pattern.finditer(text_to_search )

for match in matches:
    print(match)

# * 0 or more
# + 1 or more
# ? 0 or 1
# {3} Exact Number
#{3, 4} Range of numbers

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search )

for match in matches:
    print(match)

# | either or
# ( ) group

pattern = re.compile(r'M(r|s|rs)\.?\s[A-z]\w*')
matches = pattern.finditer(text_to_search )
for match in matches:
    print(match)

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(emails )

for match in matches:
    print(match)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls )

for match in matches:
    print(match)

matches = pattern.findall(urls ) #find group matches if groups exist

for match in matches:
    print(match)

pattern = re.compile(r'Start')
matches = pattern.match(sentence) #matches the beginning of the string, equivalent to start with ^
print(matches)

pattern = re.compile(r'sentence')
matches = pattern.search(sentence) #matches the first match in the string.
print(matches)

pattern = re.compile(r'start', re.IGNORECASE)
matches = pattern.search(sentence) #matches the first match in the string.
print(matches)
