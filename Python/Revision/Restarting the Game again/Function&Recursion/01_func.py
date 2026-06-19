def avg():
    #function definition
    a = int(input("Enter a value of a - "))
    b = int(input("Enter a value of b - "))
    c = int(input("Enter a value of c - "))
    average =(a+b+c)/3
    print(f"Average of {a},{b} & {c} is ", average)
    return average #This will take average of value and then assign this to a variable a.
a = avg() #Function call
print("Thank you")
print(a)