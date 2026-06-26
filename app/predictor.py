import pandas as pd
import pickle


with open('models/model (1).pkl', 'rb') as file:
    model= pickle.load(file)


def predicting_churn(Customer: dict):
    input_df= pd.DataFrame([Customer])
    prediction= model.predict(input_df)[0]
    if prediction == 1:
        return{
            'message' : 'Churn'
        }
    else:
        return{
            'message': 'No Churn'
        }