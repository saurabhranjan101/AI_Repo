#Show results of all arithmetic operators for two inputs.
# a = int(input("Enter value of a - "))
# b = int(input("Enter value of a - "))
# print(f"Addition of a & B is {a+b}")
# print(f"Substraction of a & B is {a-b}")
# print(f"Multiplication of a & B is {a*b}")
# print(f"Division of a & B is {a/b}")
# print(f"Remainder of a & B is {a%b}")

#Count vowels in a string

s = input("Enter a string - ")
s1 = s.lower()
vowels ="aeiou"
count = 0
for ch in s1:
    if(ch in vowels):
        count+=1
print(f"Count of vowels in {s} is {count}")