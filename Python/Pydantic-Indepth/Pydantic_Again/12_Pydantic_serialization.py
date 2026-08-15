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
temp1 = patient1.model_dump() ##This is to dump all the attributes of model into dictionary
print(temp1)
print(type(temp1))
temp2 = patient1.model_dump(include=['name','gender']) # Upu can include only name and gender. You can use exlude as well.
print(temp2)
temp3 = patient1.model_dump_json() ##This is to dump all the attributes of model into json
print(temp3)
print(type(temp3)) #Python treats json as str
temp4 = patient1.model_dump(exclude={'address':['state']})
print(temp4)