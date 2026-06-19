#Write a python function to print multiplication table of a given number

def multiply(num):
    for i in range(1,11):
        print(f"{num}X{i} =", i*num)
n = int(input("Enter a number -"))
multiply(n)      