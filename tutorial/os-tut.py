import os

print(dir(os))
print(os.getcwd())

os.chdir('/Users/udaydeshpande/Desktop')
print(os.getcwd())
print(os.listdir())
os.makedirs('nonexistingtop/subdir')
os.removedirs('nonexistingtop/subdir')

modtime = os.stat('hyperledgerfabrick.bak').st_mtime
print(modtime)

from datetime import datetime

print(datetime.fromtimestamp(modtime))

#for dirpath, dirnames, filenames in os.walk('/Users/udaydeshpande/Desktop'):
#    print('current path:', dirpath)
#    print('Directorries:', dirnames)
#    print('Files:', filenames)

print(os.environ)
print(os.environ.get('HOME'))

print(os.path.join(os.environ.get('HOME'), 'test.txt'))

print(os.path.basename('/tmp/test.txt'))

print(os.path.dirname('/tmp/test.txt'))

print(os.path.split('/tmp/tmp1/test.txt'))

print(os.path.exists('/tmp/tmp1/test.txt'))
print(os.path.isdir('/tmp/test.txt'))

print(os.path.isfile('/tmp/test.txt'))

print(os.path.splitext('/tmp/test.txt'))

