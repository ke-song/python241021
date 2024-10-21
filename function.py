# function.py

#1. defined function
def times(a, b):
    return a*b

#2. call function
result = times(3,4)
print(result)

#define function
def setValue(newValue):
    #internal value
    x = newValue
    print('함수 내부:', x)

# call
result = setValue(5)
print(result)


#local and global value 
x = 5
def func(a):
    return a+x

#call
print(func(1))

def func2(a):
    x = 10
    return a+x

#call
print(func2(1))

# default value
def times(a=10, b=20):
    return a*b

#call
print(times())
print(times(5))
print(times(5,6))

#keyword argement
def connectURI(server, port):
    strURL = 'thhp://'+server+':'+port
    return strURL

#call
print(connectURI('multi.com','80'))
print(connectURI(port='8080', server='naver.com'))




