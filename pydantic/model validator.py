from pydantic import BaseModel , EmailStr, AnyUrl, Field , field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):

    name :  str 
    email : EmailStr 
    age : int 
    married : bool
    weight : float
    contact_info: Dict[str,int]
    allergy : List[str]
 
    @model_validator(mode='after')
    def emergency_contact_validato(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_info:
            raise ValueError('patient older that 60 msut have emergency contact')
        return model

def insert_patient(pat: patient):
    print(pat.name)
    print(pat.age)
    print(pat.weight)
    print(pat.contact_info)
    print(pat.allergy)
    

patien_list = {'name':'hello', 'email' : 'hello@ici.com', 'married' : 'True' ,'age': 98, 'weight': 30, 'contact_info' : {'email': 123, 'phone' : 6454, 'emergency' : 65}, 'allergy': ['cogj','dog']}
patient1 = patient(**patien_list)
insert_patient(patient1)