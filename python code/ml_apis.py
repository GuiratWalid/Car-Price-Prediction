# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:09:38 2022

@author: Walid
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
import uvicorn


app = FastAPI()


class model_input(BaseModel):
    Year: int
    Present_Price: float
    Kms_Driven: int
    Fuel_Type: int
    Seller_Type: int
    Transmission: int
    Owner: int


# Loading the saved models
linear_regression_model = pickle.load(open('Car_Price_Model_Linear_Regression.sav','rb'))
lasso_regression_model = pickle.load(open('Car_Price_Model_Lasso_Regression.sav','rb'))

# Input Traitment
def get_Input(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    year = input_dictionary['Year']
    pre = input_dictionary['Present_Price']
    kms = input_dictionary['Kms_Driven']
    fuel = input_dictionary['Fuel_Type']
    sel = input_dictionary['Seller_Type']
    trans = input_dictionary['Transmission']
    own = input_dictionary['Owner']
    
    input_list = [year, pre, kms, fuel, sel, trans, own]
    
    return input_list


@app.post('/Car_Price_Linear_Regression')
def diabetes_pred(input_parameters: model_input):
    
    input_list = get_Input(input_parameters)
    
    prediction = linear_regression_model.predict([input_list])
    
    return prediction[0]
    
    
@app.post('/Car_Price_Lasso_Regression')
def diabetes_pred(input_parameters: model_input):
    
    input_list = get_Input(input_parameters)
    
    prediction = lasso_regression_model.predict([input_list])
    
    return prediction[0]



# Public APis
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)