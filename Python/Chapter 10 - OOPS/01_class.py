class Employee: #class creation
    language = "Py" #This is a class attributes
    salary = 1200000
harry = Employee() #object
harry.name = "Harry" #This is a object/instance attributes
rohan = Employee() #object
rohan.name = "Rohan" #This is a object/instance attributes
print(harry.name,harry.language,harry.salary)
print(rohan.name,rohan.language,rohan.salary)

#Here language and salary are class attributes and name is object attributes