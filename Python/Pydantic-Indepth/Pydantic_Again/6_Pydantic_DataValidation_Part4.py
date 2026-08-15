#Attaching Metadata in the field function
#Annotated starts with defining data type then Field function - then give constraints, title, descriptions and example
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    Name : Annotated[str, Field(max_length=50, title= 'Name of the Patient', description= 'Give the name in less than 50 chars', examples= ['Saurabh', 'Nitish'])]
    Email : EmailStr ##Email Validator Datatype from Pydantic
    linkedin_url : AnyUrl ##Link Validator Datatype from pydantic
    age : int = Field(gt=0, lt=120) #Age to be greater than 0 and less than 120.
    weight : Annotated[float, Field(gt=0, strict=True)]
    married : Annotated[bool, Field(default=None, description= ' Patient is married or not?')]
    allergies : Annotated[List[str], Field(max_length=5, description='Share the top 5 allergies patient is having.')]
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