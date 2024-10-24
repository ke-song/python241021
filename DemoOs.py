# DemoOs.py
import random

print(random.random())
print(random.random())
print()

lotto = random.sample(range(1, 46), 6)
print(lotto)


from os.path import *
print(abspath('python.exe'))
print(basename('c:\\python310\\python.exe'))

print(getsize('c:\\python310\\python.exe'))
print(exists('c:\\python310\\python.exe'))
print(isdir('c:\\python310'))


filename = 'c:\\python310\\python.exe'

if exists(filename):
    print("파일크기: {0}".format(getsize(filename)))
else:
    print('파일이 없습니다.')

import os

print("운영체제이름: {0}".format(os.name))
print("현재 작업 디렉토리: {0}".format(os.getcwd()))
# print('환경변수: {0}'.format(os.environ))


import glob
print(glob.glob('c:\\python310\\*.exe'))

lst = glob.glob(r'c:\work\*.py')
for item in lst:
    print(item)







