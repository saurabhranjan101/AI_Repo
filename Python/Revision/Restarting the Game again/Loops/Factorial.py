# #Write a program to calculate the factorial of a given number using for loop

# n = int(input("Enter a number -"))
# fact = 1
# for i in range(1,n+1): #1,2,3,4,5
#     fact = fact * i
# print(f"Factorial of {n} is {fact}")



# #5 = 5*4*3*2*1

fact = 1
n = 5
for i in range(1,n+1):
    print(f"{fact} inside a loop")
    fact = fact * i
print(f"fact outside of loop - {fact}")