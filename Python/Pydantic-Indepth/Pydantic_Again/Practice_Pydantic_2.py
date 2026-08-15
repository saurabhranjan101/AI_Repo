from typing import Annotated, Any, Dict
from pydantic import BaseModel, EmailStr, Field, field_validator


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, description='Name of the Patient')]
    age: Annotated[int, Field(gt=0, lt=120)]
    mail: EmailStr
    contact: Dict[str, Any]

    @field_validator('mail')
    @classmethod
    def email_validator(cls, value):  # Works identically!
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def name_validator(cls, value: str) -> str:
        return value.upper()


def patient_insert(p1: Patient):
    print(p1.name)
    print(p1.mail)
    print('Inserted into DB')


# Valid sample data
p2 = {
    'name': 'Saurabh',
    'age': 35,
    'mail': 'abc@hdfc.com',  # Fixed domain match
    'contact': {'phone': 123456, 'Off_Mail_Id': 'bcd@icici.com'},
}

p3 = Patient(**p2)
patient_insert(p3)