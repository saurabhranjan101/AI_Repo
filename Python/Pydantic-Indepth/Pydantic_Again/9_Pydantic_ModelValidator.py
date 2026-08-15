from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    Name : str
    Email : EmailStr ##Email Validator Datatype from Pydantic
    age : int
    weight : float
    married : bool
    allergies : List[str] #List of String
    contact_detail:Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model): #Using model you can extract all the values from model.
        if model.age > 60 and 'emergency' not in model.contact_detail:
            raise ValueError('Patient older than 60 must have emergency contact number')  
        return model

def insert_patient_data(patient: Patient):
    print(patient.Name)
    print(patient.Email)
    print(patient.age)
    print(patient.weight)
    print("Inserted")

patient_info = {
    'Name' : "Saurabh",
    'Email' : 'abc@axis.com',
    'age' : '65',
    'weight' : 72.3,
    'married' : True,
    'allergies' : ["pollen", "dust"],
    'contact_detail' : {"phone": '123456',
                        'emergency' : '22335566'}
}

patient1 = Patient(**patient_info) #Unpacking of dictionary. As soon as object gets created it calls field validator to validate if datatype is correctly mapped.
insert_patient_data(patient1)