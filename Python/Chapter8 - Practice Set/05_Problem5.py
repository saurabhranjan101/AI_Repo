'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

n = int(input("Enter a value of n ")) #Number of lines
for i in range(n,0,-1):
    print("*"*i,end="")
    print("")


#Using recurion

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
n = int(input("Enter a value of n - "))
pattern(n)
