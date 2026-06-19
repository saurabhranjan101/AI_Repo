#Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
a = int(input("Enter a value of a - "))
b = int(input("Enter a value of b - "))
c = int(input("Enter a value of c - "))
print(f"Greatest of {a}, {b} and {c} is {greatest(a,b,c)}")