#Swap two numbers without using a third variable.
a = int(input("Enter a value of A - "))
b = int(input("Enter a value of B - "))

diff = b-a
print(f"New Value of A is {a + diff} ")
print(f"New Value of B is {b - diff} ")
#10 & 20 

print("*********************************")
print("*********************************")
print("*********************************")

a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))

# XOR swap
a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("A =", a)
print("B =", b)


print("==============")
print("==============")
print("==============")

x = int(input("Enter value of X: "))
y = int(input("Enter value of Y: "))

x = x+y
y = x-y
x = x - y
print(f"Value of X: {x} ")
print(f"Value of Y: {y} ")