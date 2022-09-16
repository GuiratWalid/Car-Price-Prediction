# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:25:18 2022

@author: Walid
"""

import json
import requests


url1 = 'http://0389-102-159-185-202.ngrok.io/Car_Price_Linear_Regression'

url2 = 'http://localhost:8000/Car_Price_Lasso_Regression'

input_data_for_model = {
    
    'Year': 2011,
    'Present_Price': 4.15,
    'Kms_Driven': 5200,
    'Fuel_Type': 0,
    'Seller_Type': 0,
    'Transmission': 0,
    'Owner': 0,

    }

# Linear Regression Model
input_json = json.dumps(input_data_for_model)

response = requests.post(url1, data= input_json)

print("Linear Regression: ",response.text)


# Lasso Regression Model
input_json = json.dumps(input_data_for_model)

response = requests.post(url2, data= input_json)

print("Lasso Regression: ",response.text)