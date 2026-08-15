from pydantic import BaseModel
class Patient(BaseModel):
    Name : str
    age : int
    weight : float

def insert_patient_data(patient: Patient):
    print(patient.Name)
    print(patient.age)
    print(patient.weight)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.Name)
    print(patient.age)
    print(patient.weight)
    print("Updated")

patient_info = {
    'Name' : "Saurabh",
    'age' : 33,
    'weight' : 72.3
}

patient1 = Patient(**patient_info) #Unpacking of dictionary
insert_patient_data(patient1)
update_patient_data(patient1)