from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    Name : str = Field(max_length= 50)
    Email : EmailStr ##Email Validator Datatype from Pydantic
    linkedin_url : AnyUrl ##Link Validator Datatype from pydantic
    age : int = Field(gt=0, lt=120) #Age to be greater than 0 and less than 120.
    weight : float = Field(gt=0) #Weight to be greater than 0
    married : bool = False
    allergies : Optional[List[str]] = Field(max_length=5) #This should contain only 5 allergies
    contact_detail:Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.Name)
    print(patient.Email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.married)
    print("Inserted")

def update_patient_data(patient: Patient): 
    print(patient.Name)
    print(patient.age)
    print(patient.weight)
    print("Updated")

patient_info = {
    'Name' : "Saurabh",
    'Email' : 'abc@gmail.com',
    'linkedin_url' : 'http://linked.com/1322',
    'age' : 33,
    'weight' : 72.3,
    #'married' : True,
    'allergies' : ["pollen", "dust"],
    'contact_detail' : {"phone": '123456'}
}

patient1 = Patient(**patient_info) #Unpacking of dictionary
insert_patient_data(patient1)
update_patient_data(patient1)