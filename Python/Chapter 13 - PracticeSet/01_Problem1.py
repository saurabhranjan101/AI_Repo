#A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
#Write a program to filter a list of numbers which are divisible by 5.
from functools import reduce
l = [7,14,21,28,35,42,49,56,63,70]
def prob1(x):
    if(x%5 == 0):
        return True
    return False
prob = filter(prob1,l)
print(list(prob))