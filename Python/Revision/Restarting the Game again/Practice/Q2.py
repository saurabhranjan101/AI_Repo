#Calculate area of a circle given its radius.
r = int(input("Enter value of radius - "))
#area = 3.14 * r *r
print(f"Area of circle - {3.14 * r *r}")

s = input("Enter a string - ")
s1 = s.lower()
print(s1)
s2 = s1[::-1]
if(s1 == s2):
    print("Palindrome")
else:
    print("Not a palindrone")