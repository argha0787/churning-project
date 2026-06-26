from fastapi import FastAPI
from app.schema import CustomerDetails
from app.predictor import predicting_churn

app= FastAPI()

@app.get('/')
def home():
    return{
        'message': 'the churning4 app is running'
    }

@app.post('/predict')
def prediction(data: CustomerDetails):
    flag= data.model_dump()
    predictor= predicting_churn(flag)
    return{
        'message': predictor
    }