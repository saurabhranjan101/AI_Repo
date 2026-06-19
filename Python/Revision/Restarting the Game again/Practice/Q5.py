# #Count vowels in a string.
# x = input("Enter a string - ")
# y = x.count("a")
# z = x.count("e")
# a = x.count("i")
# b = x.count("o")
# c = x.count("u")
# print(f"Number of vowels in string is {y+z+a+b+c}")

x = input("Enter a string - ")
x = x.lower()
count = 0
vowels = "aeiou"
for ch in x:
    if(ch in vowels):
        count +=1
print(f"Count of vowels is {count} ")


#Reverse a list without using reverse() or slicing.
l = [2,3,4,5]
rev = []
for i in l:
    rev.insert(0,i)
print(rev)