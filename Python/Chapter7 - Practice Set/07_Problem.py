'''
Write a program to print the following star pattern.
 *
***
***** for n = 3
'''

n = int(input("Enter a number - ")) #This will be number of lines.
for i in range(1,n+1): #i =1,2,3
    print(" "* (n-i), end="") #this is for having a space in the pattern
    print("*"* (2*i-1),end="")#this is for printing a star. end="" - this won't create a new line.
    print("") #this will create a new line