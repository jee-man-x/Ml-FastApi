from fastapi.responses import JSONResponse
from fastapi import FastAPI
from schema.user_input import UserInput
import pandas as pd
from model.predict import predict_output,model,MODEL_VERSION

    
app=FastAPI()

#human readable    
@app.get('/')
def home_page():
    return {"message":"incurence prediction Api"}

#machine readable
@app.get('/health')
def health_check():
    return {
        'status':'ok',
        'version':MODEL_VERSION,
        'model_loaded':model is not None
    }

@app.post('/predict')
def predict_premiun(data:UserInput):
    
    user_input=pd.DataFrame([{
        'age':data.age,
        'sex': data.sex,
        'bmi':data.bmi,
        'smoker':data.smoker,
        'region':data.region,
        'expenses':data.expenses
    }])
    try:
        prediction=predict_output(user_input)
            
        return JSONResponse(status_code=200,content={"prediction_category": str(prediction)})
    
    except Exception as e :
        return JSONResponse(status_code=500,content=str(e))
            
    
    
