"""
Write a program to print the following star pattern: 
*
**
*** for n = 3
"""

n= int(input("Enter a number - ")) #This will be number of lines.
for i in range(1,n+1):
    print("*" *i,end="")
    print(" " *(2*i-1),end="")
    print("")

