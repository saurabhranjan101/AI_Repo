n = int(input("Enter a number - "))
i = 1
mod = 1
for i in range(1,n+1):
    mod = mod * i
print(f"Factorial of {n} is {mod}")