from fastapi import FastAPI, Query, Path, HTTPException
import json
app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

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