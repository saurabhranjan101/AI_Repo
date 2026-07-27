from pydantic import BaseModel
class Employee(BaseModel):
    name : str
    age : int
    
def insert_employee(employee : Employee):
    print(employee.name)
    print(employee.age)
    print("Inserted into DB")

def update_employee(employee : Employee):
    print(employee.name)
    print(employee.age)
    print("Updated into DB")

employee_data = {
    'name' : "Saurabh",
    'age': 34    
    }
employee1 = Employee(**employee_data)
insert_employee(employee1)
update_employee(employee1)