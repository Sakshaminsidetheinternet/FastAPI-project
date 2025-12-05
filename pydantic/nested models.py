from pydantic import BaseModel

class Adddress(BaseModel):
    city : str
    state : str
    pin : int

class Patient(BaseModel):
    name : str
    age : int
    address : Adddress

adress = {'city' : 'delhi', 'state' : 'delhi', 'pin' : 686  }
Adress1 = Adddress(**adress)

patient_info = {'name' : 'log', 'age' : 44, 'address' : Adress1}
patient1 = Patient(**patient_info)
#print(patient1)
print(patient1.address.city)
print(patient1.name)