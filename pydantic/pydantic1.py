from pydantic import BaseModel
from typing import List, Dict

class patient(BaseModel):

    name : str
    age : int
    weight : float
    contact_info: Dict[str,int]
    allergy : List[str]

def insert_patient(pat: patient):
    print(pat.name)
    print(pat.age)
    print(pat.weight)
    print(pat.contact_info)
    print(pat.allergy)
    

patien_list = {'name':'hello', 'age': 30, 'weight': 30, 'contact_info' : {'email': 123, 'phone' : 6454}, 'allergy': ['cogj','dog']}
patient1 = patient(**patien_list)
insert_patient(patient1)