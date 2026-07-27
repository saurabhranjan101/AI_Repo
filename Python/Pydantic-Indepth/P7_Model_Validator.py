from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated
class Employee(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str] #By this - we are making sure that we are passing ONLY string inside List.
    contact_detail : Dict[str, str] #By this - we are making sure that we are passing ONLY string inside Dictionary.

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_detail:
            raise ValueError('Patient older than 60 must have emergency contact')
        return model

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
    'email': 'abc@hdfc.com',
    'age' : 64,
    'weight' : 72.4,
    'married' :True,
    'allergies': ['Eggs','Dust'],
    'contact_detail' : {'Email' :'abc@abc.com',
                        'Phone_Number' : '1223355',
                        'emergency':'234567'}
}
employee1 = Employee(**employee_info) ##Field Validator.
employee_insert(employee1)
employee_update(employee1)