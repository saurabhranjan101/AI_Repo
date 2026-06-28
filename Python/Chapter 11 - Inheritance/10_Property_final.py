class Employee:
    a = 1
    name = "Saurabh"
    @classmethod
    def show(cls):
        print(f"Value of A is {cls.a}")
        #print(f"Value of name is {cls.name}")
    
    #Property decorator
    @property #Method name with property decorator are called as getter method.
    def name(self):
        print("Hello Saurabh")
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = Employee()
e.a = 45
e.name = "Harry Khan"
print(e.fname, e.lname)
e.show()