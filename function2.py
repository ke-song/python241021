#more comp
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union('HAM','EGG'))
print(union('HAM','EGG','SPAM'))


#lambda function

g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print( (lambda x:x*x)(3) )

print( globals())
print( dir())

