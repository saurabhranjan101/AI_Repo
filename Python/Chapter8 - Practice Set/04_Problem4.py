#Write a recursive function to calculate the sum of first n natural numbers.

def recursum(n):
    if(n==1):
        return 1
    return n + recursum(n-1)
n = int(input("Enter a number - "))
print(f"Sum of {n} natural number using recursion is {recursum(n)}")