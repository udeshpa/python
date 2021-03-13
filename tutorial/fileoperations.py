f = open('test.txt', 'r') #w write, a append, r+ read/write
print(f.name, f.mode)
f.close()

#Now using context manager

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

print(f.closed)

with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

with open('test.txt', 'r') as f:
    f_contents = f.read(8) # read 100 characters
    print(f_contents)

with open('test.txt', 'r') as f:
    size_to_read = 8
    f_contents = f.read(size_to_read)  # read 100 characters
    while len(f_contents) >0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

with open('test.txt', 'r') as f:
    f_contents = f.read(8)
    print(f.tell())

    f.seek(0)
    f_contents = f.read(15)
    print(f.tell())

with open('test2.txt', 'w') as f:  #will create a new file if one does not exists, overwrite if it does
    f.write('Test')
    f.seek(0)
    f.write('R')

import os
os.remove('test2.txt')

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('/Users/udaydeshpande/Downloads/myphoto.jpeg', 'rb') as rf:
    with open('myphoto.jpeg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


