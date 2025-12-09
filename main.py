from fastapi import FastAPI, Query, Path, HTTPException
#import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated ,Literal ,Optional

class Patient(BaseModel):
    id : Annotated[str, Field(..., description='id of the patient', examples='P001')]
    name : Annotated[str, Field(..., description='Name of the patient')]
    city : Annotated[str, Field(..., description='name of the city' )]
    age : Annotated[int, Field(..., gt=0, lt=120, description='age of the patient between 0-120')]
    gender : Annotated[Literal['male', 'female', 'others'], Field(...,description='GEnder of the patient')]

    height : Annotated[float, Field(...,description='height of the patient', gt=0)]
    weight : Annotated[float, Field(...,description='weight of the patient', gt=0)]


   
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi<18.5:
            return 'Under weight'
        elif self.bmi<30:
            return 'normal' 
        else:
            return 'obese'

class Patientupdate(BaseModel):
    
    name : Annotated[Optional[str], Field(default=None)]
    city : Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int], Field(default=None, gt=0)]
    gender : Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None)]

    height : Annotated[Optional[float], Field(default=None, gt=0)]
    weight : Annotated[Optional[float], Field(default=None, gt=0)]


app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patient.json','w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {"message : hello"}

@app.get("/view")
def h():
    data = load_data()
    return {"yoloyolo"}, data   

@app.get('/patient/{patient_id}')
def patient(patient_id: str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error : not found1"}

@app.get('/sort')
def sort_patient(query_sort: str = Query(..., description = 'sort on weight, height'), order: str = Query('asc', description='sorty by ascending or desending order')) :
    valid = ['height', 'weight', 'bmi']
    if query_sort not in valid:
        raise HTTPException(status_code = 400, detail = f'invalid field select from {valid}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = 'select from asc or desc')
    data = load_data()
    sort_asc = True if order=='desc' else False
    sorted_data = sorted(data.values(),key = lambda x: x.get(query_sort,0), reverse = sort_asc)

    return sorted_data

@app.post('/create')
def create_patient(patient : Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='already exist')
    
    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201, content={'message':'patient created'})

@app.post('/update{patient_id}')
def update_patient(patient_id : str, patient_updated: Patientupdate ):
    data = load_data()
    existing_info = data[patient_id]
    updated_info = patient_updated.model_dump(exclude_unset=True)
    for key, value in update_patient:
        existing_info[key] = value
    existing_info['id'] = patient_id
    object_infoo = Patient(**existing_info)
    existing_info = object_infoo.model_dump(exclude='id')
    data[patient_id] = existing_info
    save_data(data)
    return JSONResponse(status_code=200, content='message: patient updated')