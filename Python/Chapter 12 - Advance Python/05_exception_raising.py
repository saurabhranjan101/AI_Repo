a = int(input("Enter a number - "))
b = int(input("Enter a second number - "))
if(b == 0):
    raise ZeroDivisionError("Program is not meant to be divided by 0")
else:
    print(f"Division of a/b is {a/b}")