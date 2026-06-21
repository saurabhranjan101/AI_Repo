class Employee: #class creation
    language = "Python" #This is a class attributes
    salary = 1200000
    def __init__(self, name, salary, language): #dunder method which is automatically called when object is created
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    def getInfo(self): #self parameter
        print(f"The language is {self.language}. Salary is {self.salary}")
    @staticmethod #This is used when we don't have to pass self parameter or we don't require anything from object
    def greet():
        print("Good Morning")
harry = Employee("Harry",1300000,"Javascript") #object is getting created with attributes and then dunder method will get automatically called by passing 3 attributes.
harry.name = "Harry"
print(harry.name, harry.language, harry.salary)