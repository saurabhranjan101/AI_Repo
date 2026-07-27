#Required & Optional fields
from pydantic import BaseModel
from typing import List, Dict, Optional
class Employee(BaseModel):
    name : str
    age : int
    weight : float
    married : bool = False #Defaut value is False.
    allergies : Optional[List[str]] = None #By this - we are making sure that we are passing ONLY string inside List.This is Optional Fieldand we have to pass None as default value
    contact_detail : Dict[str, str] #By this - we are making sure that we are passing ONLY string inside Dictionary.

def employee_insert(employee:Employee):
    print(employee.name)
    print(employee.age)
    print(employee.weight)
    print(employee.married)
    print(employee.allergies)
    print(employee.contact_detail)
    print("Data Inserted")

def employee_update(employee:Employee):
    print(employee.name)
    print(employee.age)
    print(employee.weight)
    print(employee.married)
    print(employee.allergies)
    print(employee.contact_detail)
    print("Data Updated")

employee_info = {
    'name':'Saurabh',
    'age' : 34,
    'weight' : 72.4,
    ##'married' :True,
    ##'allergies': ['Eggs','Dust'],
    'contact_detail' : {'Email' :'abc@abc.com',
                        'Phone_Number' : '1223355'}
}
employee1 = Employee(**employee_info)
employee_insert(employee1)
employee_update(employee1)