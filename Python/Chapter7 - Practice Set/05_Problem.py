#Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter a number - "))
i = 0
sum = 0
while(i<=n):
    sum = sum+i
    i = i+1
print("Sum of each of value -", sum)


m = int(input("Enter a number - "))
i = 0
sum1 = 0
while(i<=m):
    sum1+= i
    i = i+1
print(f"Sum of {m} is {sum1}")