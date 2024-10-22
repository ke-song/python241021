lst = [100,200,300]

for i in lst:
    print(i)
print()

print(list(range(10)))
print(list(range(2000,2005)))
print(list(range(1,32)))
print()

lst = list(range(1,11))
print(lst)
print([i**2 for i in lst if i > 5])
tp = ('apple','orange','kiwi')
d={100:'apple',200:'orange'}
print([v.upper() for v in d.values()])
print()

lst = [10,25,30]
itemL = filter(None, lst)
for i in itemL:
    print('item:{0}'.format(i))

def getBiggerThan20(i):
    return i > 20
print()

itemL = filter(getBiggerThan20, lst)
for i in itemL:
    print('item:{0}'.format(i))
print()

itemL = filter(lambda x:x>25, lst)
for i in itemL:
    print('item:{0}'.format(i))
print()



