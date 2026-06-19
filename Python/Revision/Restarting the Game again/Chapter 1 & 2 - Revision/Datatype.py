a = 12
b = 25.6
c = "Saurabh"

# print(type(a))
# print(type(b))
# print(type(c))
#Input function --this takes input from user and store as string.

d = int(input("Enter a value - ")) ##this is type casting
print(type(d))

#Let's add two numbers

e = int(input("Enter a value of e - "))
f = int(input("Enter a value of f - "))
print("Sum of e & f is ", e+f)


##Write a python program to find remainder when a number is divided by z.
print("Remainder of e & f is ", e%f)

#Use comparison operator to find out whether ‘e’ given variable e is greater than ‘f’ or not
if(e>f):
    print("e is greater than f")
elif(e == f):
    print("e is equal to f")
else:
    print("e is less than f")

print("Let's find the average of e & f - ", (e+f)/2)


#Write a python program to calculate the square of a number entered by the user.
print("Square of e is ", e*e)