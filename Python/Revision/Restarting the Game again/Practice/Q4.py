#Check if a string is a palindrome.
x = input("Enter a string - ")
y = x[::-1] #this is how we reverse string. Start, Stop and step - String slicing concept
if(x == y):
    print("Palindrome")
else:
    print("No Palindrome") 

#Replace spaces with underscores.

s = input("enter a sentence")
s1 = s.replace(" ","_")
print(s1)