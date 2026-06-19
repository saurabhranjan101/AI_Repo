#p = input("Enter a name")
# q = p.lower()
# w = q[::-1]
# if(q == w):
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# print("======================")
# print("======================")

# s = input("Enter a name")
# r = s[::-1]
# print(r)

p = input("Enter a Sentence - ")
v = c = d = s = 0
v = "aeiou"
for i in p:
    if(i in v):
        v+=1
    elif(c.isalpha()):
        c+=1
    elif(c.isdigit()):
        d+=1
    else:
        s +=1
print(f"Vowels -{v}")
print(f"Consonants -{v}")
print(f"Digits -{v}")
print(f"Special Characters -{v}")