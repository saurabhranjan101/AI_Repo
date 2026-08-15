from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    Name : str
    Email : EmailStr ##Email Validator Datatype from Pydantic
    linkedin_url : AnyUrl ##Link Validator Datatype from pydantic
    age : int
    weight : float
    married : bool = False
    allergies : Optional[List[str]] = None #List of String
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
    ##'allergies' : ["pollen", "dust"],
    'contact_detail' : {"phone": '123456'}
}

patient1 = Patient(**patient_info) #Unpacking of dictionary
insert_patient_data(patient1)
update_patient_data(patient1)