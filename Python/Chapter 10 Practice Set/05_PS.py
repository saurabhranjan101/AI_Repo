#Create a class with a class attribute a; 
# create an object from it and set ‘a’ directly using 
# ‘object.a = 0’. Does this change the class attribute?

class xyz:
    a = 4
b = xyz()
print(b.a) #prints class attri as instance attri is not present
b.a = 0 #prints instance attri as instance attri is present
print(b.a)
print(xyz.a) #this prints the class attribute