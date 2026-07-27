from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated
class Employee(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str] #By this - we are making sure that we are passing ONLY string inside List.
    contact_detail : Dict[str, str] #By this - we are making sure that we are passing ONLY string inside Dictionary.

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1] #if value is abc@gmail.com then it will split from @ and -1 wil give the domain.
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

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
    'age' : 34,
    'weight' : 72.4,
    'married' :True,
    'allergies': ['Eggs','Dust'],
    'contact_detail' : {'Email' :'abc@abc.com',
                        'Phone_Number' : '1223355'}
}
employee1 = Employee(**employee_info) ##Field Validator.
employee_insert(employee1)
employee_update(employee1)