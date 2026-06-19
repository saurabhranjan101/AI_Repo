#Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter a number to multiply in reverse order - "))
for i in range(1,11):
    print(f"{n}X{11-i}={(11-i)*n}")