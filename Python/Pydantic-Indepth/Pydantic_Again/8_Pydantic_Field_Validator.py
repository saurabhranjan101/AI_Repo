from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    Name : str
    Email : EmailStr ##Email Validator Datatype from Pydantic
    age : int
    weight : float
    married : bool
    allergies : List[str] #List of String
    contact_detail:Dict[str, str]

    @field_validator('Email')
    @classmethod
    def email_validator(cls, value): #cls = method inside the class can be used in this method. Value = Email's value
        valid_domains = ['hdfc.com', 'icici.com']
        #abc@gmail.com -> we have to extract gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            return ValueError('Not a valid domain')
        return value

    @field_validator('Name')
    @classmethod
    def tansform_name(cls, value):
        return value.upper()

    @field_validator('age', mode= 'before')
    @classmethod
    def age_validator(cls, value):
        if value > 0 and value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 & 100')


def insert_patient_data(patient: Patient):
    print(patient.Name)
    print(patient.Email)
    print(patient.age)
    print(patient.weight)
    print("Inserted")

patient_info = {
    'Name' : "Saurabh",
    'Email' : 'abc@axis.com',
    'age' : '33',
    'weight' : 72.3,
    'married' : True,
    'allergies' : ["pollen", "dust"],
    'contact_detail' : {"phone": '123456'}
}

patient1 = Patient(**patient_info) #Unpacking of dictionary. As soon as object gets created it calls field validator to validate if datatype is correctly mapped.
insert_patient_data(patient1)