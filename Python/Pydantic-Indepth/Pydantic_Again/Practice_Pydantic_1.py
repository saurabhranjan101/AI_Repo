from pydantic import BaseModel, field_validator, Field, EmailStr, AnyUrl
from typing import List, Dict, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, description="Name of the Patient")]
    age : int = Annotated[int, Field(gt=0, lt=120)]
    weight : float = Annotated[float, Field(gt=0)]
    email : EmailStr
    LinkedIn : AnyUrl
    allergy : List[str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        email_domain = ['hdfc.com','axis.com']
        domain = value.split('@')[-1]
        if domain in email_domain:
            return value
        return ValueError('Invalid Domain')

    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()

def insert_patient(p1:Patient):
    print(p1.name)
    print(p1.email)

patient_info = {
    'name' :'Saurabh',
    'age' :33,
    'weight' : 72.8,
    'email' : 'abc@hdfc.com',
    'LinkedIn': 'http://hdffdvchdhcd/1233',
    'allergy' : ['eggs','dust']
}
patient1 = Patient(**patient_info)
insert_patient(patient1)