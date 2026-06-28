class employee:
    a = 1
class programmer(employee):
    b = 2
class Manager(programmer):
    c = 3
o = employee()
print(f"{o.a}") #Prints a attributes
#print(f"{o.b}") #Error as there is no attribute

o2 = programmer()
print(f"{o2.a} and {o2.b}")

o3 = Manager()
print(f"{o3.a}, {o3.b} and {o3.c}")