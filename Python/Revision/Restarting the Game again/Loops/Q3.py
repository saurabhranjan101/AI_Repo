n = int(input("Enter a number"))
for i in range(2,n):
    if (n%i) == 0:
        print("Not a prime")
        break
else:
    print("Prime Number")

for j in range(2,3):
    print(j)