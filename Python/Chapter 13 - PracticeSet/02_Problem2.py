##Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
l = [7,14,21,28,35,42,49,56,63,70]
def greater(a, b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))