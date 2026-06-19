a = int(input("Enter your age "))
#If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("You are good")
elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 which is not valid")

else:
    print("You are below the age of consent")

print("End of Program")