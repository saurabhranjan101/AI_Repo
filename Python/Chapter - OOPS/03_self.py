class Employee: #class creation
    language = "Python" #This is a class attributes
    salary = 1200000
    def getInfo(self): #self parameter
        print(f"The language is {self.language}. Salary is {self.salary}")
    @staticmethod #This is used when we don't have to pass self parameter or we don't require anything from object
    def greet():
        print("Good Morning")
harry = Employee() #object
harry.language = "Javascript" #This is a object/instance attributes and this will get precedense over class attributes during retrieval & assignment
harry.getInfo() ##This will fail as call happen like -> Employee.getInfo("harry"). To fix we'll use self as argument of getInfo function.
Employee.getInfo(harry) #this is same as harry.getInfo()
harry.greet()