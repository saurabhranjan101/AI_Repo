'''
     1
    212
   32123
  4321234
 543212345
'''

n = int(input("Enter a number - "))
for i in range(1, n+1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print descending numbers from i down to 1
    for j in range(i, 0, -1):
        print(j, end="")

    # Print ascending numbers from 2 up to i
    for j in range(2, i+1):
        print(j, end="")

    # Move to next line
    print()
