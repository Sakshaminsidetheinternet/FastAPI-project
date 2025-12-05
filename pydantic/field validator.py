from pydantic import BaseModel , EmailStr, AnyUrl, Field , field_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):

    name :  str 
    email : EmailStr 
    age : int 
    married : bool
    weight : float
    contact_info: Dict[str,int]
    allergy : List[str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        domain = ['hdfc.com', 'sbi.com']
        value_name = value.split('@')[-1]
        if value_name not in domain:
            raise ValueError('not a valid domain')
        return value  

def insert_patient(pat: patient):
    print(pat.name)
    print(pat.age)
    print(pat.weight)
    print(pat.contact_info)
    print(pat.allergy)
    

patien_list = {'name':'hello', 'email' : 'hello@ici.com', 'married' : 'True' ,'age': 30, 'weight': 30, 'contact_info' : {'email': 123, 'phone' : 6454}, 'allergy': ['cogj','dog']}
patient1 = patient(**patien_list)
insert_patient(patient1)