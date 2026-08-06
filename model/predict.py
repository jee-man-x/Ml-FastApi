import pandas as pd
import pickle

#import ml file 
with open('model/model.pkl','rb') as f:
    model=pickle.load(f)

#MLflow
MODEL_VERSION='1.0.0'

class_lable=model.classes_.tolist()

def predict_output(user_input:dict):
   

   #input_df=pd.DataFrame([user_input])
   prediction_class=model.predict(user_input)[0]
   
   probebility=model.predict_proba(user_input)[0]
   confidence=max(probebility)
   
   class_probs=dict(zip(class_lable,map(lambda p:round(p,4),probebility)))
   
   return {
       "prediction_category":prediction_class,
       "confidence":round(confidence,4),
       "class_prob":class_probs
   }
