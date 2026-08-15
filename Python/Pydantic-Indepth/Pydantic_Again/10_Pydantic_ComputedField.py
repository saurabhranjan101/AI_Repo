from pydantic import BaseModel, computed_field, EmailStr
from typing import List, Dict

class Patient(BaseModel):
    name : str
    age : int
    weight : float #kg
    height : float #mtr
    married : bool
    allergies : List[str]
    contact_detail: Dict[str, str]
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print('BMI', patient.calculate_bmi)

patient_info = {
    'name' : "Saurabh",
    'age' : '33',
    'weight' : 72.3,
    'height' : 1.72,
    'married' : True,
    'allergies' : ["pollen", "dust"],
    'contact_detail' : {"phone": '123456'}
}

patient1 = Patient(**patient_info) #Unpacking of dictionary. As soon as object gets created it calls field validator to validate if datatype is correctly mapped.
insert_patient_data(patient1)