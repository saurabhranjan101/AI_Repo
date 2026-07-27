'''
12345
1234
123
12
1
'''
n = int(input("Enter a number - "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()
    n -=1