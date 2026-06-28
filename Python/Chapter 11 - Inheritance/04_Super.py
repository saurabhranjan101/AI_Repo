class employee:
    def __init__(self):
        print("Contructor of employee")
    a = 1
class programmer(employee):
    def __init__(self):
        print("Contructor of programmer")
    b = 2
class Manager(programmer):
    def __init__(self):
        super().__init__() #this will call the constructor of parent class - super class
        print("Contructor of Manager")
    c = 3
o = employee()
print(f"{o.a}") #Prints a attributes

o2 = programmer()
print(f"{o2.a} and {o2.b}")

o3 = Manager()
print(f"{o3.a}, {o3.b} and {o3.c}")