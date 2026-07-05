from functools import reduce
#Map Example
l = [1,2,3,4,5]
square = lambda x:x*x #Square is a lamda function
sqlist = map(square,l) ##this maps function-square to list l
print(list(sqlist))

#Filter example
def even(n):
    if(n%2 == 0):
        return True
    return False
onlyEven = filter(even, l)
print(list(onlyEven))

#Reduce Example
def sum(a,b):
    return a+b
print(reduce(sum, l))

mul = lambda x,y:x*y
print(reduce(mul,l))