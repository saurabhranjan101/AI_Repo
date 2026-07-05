#Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
# a = int(input("Enter a value of A  - "))
# b = int(input("Enter a value of B  - "))
# if(b == 0):
#     raise ZeroDivisionError("Program is not meant to be divided by 0 ")
# else:
#     print(f"Division of a/b is {a/b}")

try:
    a = int(input("Enter a value of A  - "))
    b = int(input("Enter a value of B  - "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")