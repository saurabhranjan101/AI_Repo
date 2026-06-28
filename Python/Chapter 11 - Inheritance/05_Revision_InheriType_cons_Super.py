#Inheritance & It's type
#Single Inheritance
# class parent1:
#     a = 1
#     def par1(self):
#         print("Method of Parent1")
# class child(parent1):
#     b = 1
#     def par2(self):
#         print("Method of Child")
# c = parent1()
# d = child()
# d.par1() 
# d.par2()

#Multiple Inheritance
# class parent1:
#     a = 1
#     def par1(self):
#         print("Method of Parent1")

# class parent2:
#     e = 2
#     def par2(self):
#         print("Method of Parent2")

# class child(parent1, parent2):
#     f = 3
#     def par2(self):
#         print("Method of Child")
# g = child()
# print(g.a, g.e, g.f)


#Multi level inheritance
# class parent1:
#     a = 1
#     def par1(self):
#         print("Method of Parent1")

# class parent2(parent1):
#     e = 2
#     def par2(self):
#         print("Method of Parent2")

# class child(parent2):
#     f = 3
#     def par2(self):
#         print("Method of Child")
# g = child()
# print(g.f, g.e, g.a) #Using an object of child we can fetch data from parent1 & parent2


#Contructor
# class parent1:
#     a = 1
#     def __init__(self,fname):
#         self.fname = fname
#         print(f"Father name is {fname}")
#     def par1(self):
#         print("Method of Parent1")

# class parent2(parent1):
#     e = 2
#     def __init__(self,mname):
#         self.mname = mname
#         print(f"Mother name is {mname}")
#     def par2(self):
#         print("Method of Parent2")

# class child(parent2):
#     f = 3
#     def __init__(self,cname):
#         self.cname = cname
#         print(f"Child name is {cname}")
#     def par2(self):
#         print("Method of Child")
# g = child("Monu")
# h = parent2("Meena")
# i = parent1("Rajeev")

class parent1:
    a = 1
    def __init__(self,fname):
        self.fname = fname
        print(f"Father name is {fname}")
    def par1(self):
        print("Method of Parent1")

class parent2(parent1):
    e = 2
    def __init__(self,mname,fname):
        super().__init__(fname) ##this calls the constructor of super class
        self.mname = mname
        self.fname = fname
        print(f"Mother name is {mname}")
    def par2(self):
        super().par1()
        print("Method of Parent2")

class child(parent2):
    f = 3
    def __init__(self,cname,mname,fname):
        super().__init__(mname,fname) ##this calls the constructor of super class
        super().par2()
        self.cname = cname
        self.fname = fname
        print(f"Child name is {cname}")
    def par2(self):
        print("Method of Child")
child1 = input("Enter your child name - ")
mother = input("Enter your mother name - ")
father = input("Enter your mother name - ")

g = child(child1,mother,father)

#Class Method
class abc:
    x = 1
    @classmethod
    def show(cls):
        print(f"Value is X is {cls.x}")
y = abc()
x = 27
y.show()