from pydantic import BaseModel , EmailStr, AnyUrl, Field , field_validator, computed_field,  model_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):

    name :  str 
    email : EmailStr 
    age : int 
    married : bool
    height : float
    weight : float
    contact_info: Dict[str,int]
    allergy : List[str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def insert_patient(pat: patient):
    print(pat.name)
    print(pat.age)
    print(pat.weight)
    print(pat.contact_info)
    print(pat.allergy)
    print(pat.bmi)
    

patien_list = {'name':'hello', 'email' : 'hello@ici.com', 'married' : 'True' ,'age': 98, 'weight': 30, 'height' : 80 , 'contact_info' : {'email': 123, 'phone' : 6454, 'emergency' : 65}, 'allergy': ['cogj','dog']}
patient1 = patient(**patien_list)
insert_patient(patient1)