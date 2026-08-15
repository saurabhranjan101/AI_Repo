from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin: str
class patient(BaseModel):
    name : str
    gender : str
    age : int
    address : Address

address_dict = {
    'city' : 'Ranchi',
    'state' : 'Jharkhand',
    'pin' : '829106'
}
address1 = Address(**address_dict)
patient_dict = {'name' : 'Saurabh',
            'gender' : 'Male',
            'age' : 33,
            'address' : address1}
patient1 = patient(**patient_dict)
print(patient1)
print(patient1.address.city)
print(patient1.address.pin)