class Employee: #class creation
    language = "Python" #This is a class attributes
    salary = 1200000
harry = Employee() #object
harry.language = "Javascript" #This is an object/instance attributes and this will get precedense over class attributes during retrieval & assignment
print(harry.language,harry.salary)