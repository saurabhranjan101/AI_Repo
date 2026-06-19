#Write a python function to print multiplication table of a given number.

'''
5*1
5*2
5*3
5*4


'''

def muliplication(n):
    for i in range(1,11):
        print(f"{n}X{i} = {n*i}")
n = int(input("Enter a value of n - "))
muliplication(n)