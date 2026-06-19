a = int(input("Enter your age "))
#If statement number 1
if(a%2 == 0):
    print("a is even")
#End of If statement number 1

#If statement number 2
if(a>=18):
    print("You are above the age of consent")
    print("You are good")
elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 which is not valid")

else:
    print("You are below the age of consent")
#End of If statement number 2
print("End of Program")