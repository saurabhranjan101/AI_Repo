from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional
class Employee(BaseModel):
    name : str
    email : EmailStr
    linkedin_url : AnyUrl
    age : int
    weight : float
    married : bool = False #Defaut value is False.
    allergies : Optional[List[str]] = None #By this - we are making sure that we are passing ONLY string inside List.This is Optional Fieldand we have to pass None as default value
    contact_detail : Optional[Dict[str, str]]#By this - we are making sure that we are passing ONLY string inside Dictionary.
def employee_insert(employee:Employee):
    print(employee.name)
    print(employee.email)
    print(employee.linkedin_url)
    print(employee.age)
    print(employee.weight)
    print(employee.married)
    print(employee.allergies)
    #print(employee.contact_detail)
    print("Data Inserted")

def employee_update(employee:Employee):
    print(employee.name)
    print(employee.email)
    print(employee.linkedin_url)
    print(employee.age)
    print(employee.weight)
    print(employee.married)
    print(employee.allergies)
    #print(employee.contact_detail)
    print("Data Updated")

employee_info = {
    'name':'Saurabh',
    'email': 'abc@gmail.com',
    'linkedin_url': 'https://linkedin.com/1233',
    'age' : 34,
    'weight' : 72.4,
    'contact_detail' : {'Phone_Number' : '1223355'}
    ##'married' :True,
    ##'allergies': ['Eggs','Dust'],
    # 'contact_detail' : {#'Email' :'abc@abc.com',
    #                     'Phone_Number' : '1223355'}
}
employee1 = Employee(**employee_info) ##here we are unpacking the dictionary
employee_insert(employee1)
employee_update(employee1)