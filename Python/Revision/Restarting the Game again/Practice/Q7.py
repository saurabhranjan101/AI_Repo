#Find max and min in a list
# l = [20,10,45,85,5]
# print(max(l))
# print(min(l))

#Reverse a list without using reverse() or slicing.
l = [20,10,45,85,5]
rev = []
for item in l:
    rev.insert(0,item)
print(rev)