def avg(): #Here we are defining a function and below are set of statements under function.
    a = int(input("Enter a number - "))
    b = int(input("Enter a number - "))
    c = int(input("Enter a number - "))
    average = (a+b+c)/3
    print(average)
    return average
a = avg() #This is function call.
print(f"hello, Your average is {a}")
avg() #This is function call.
print("Thanks")
avg() #This is function call.
print("You")