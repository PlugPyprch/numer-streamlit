import streamlit as st
import pandas as pd
import numpy as np 
import requests
import json 

def history_main():
    st.markdown("<h1 style='text-align: center; color: grey;'>History</h1>", unsafe_allow_html=True)
    show_get_data()
    
def show_get_data():
    x = requests.get('https://numer-api-db.herokuapp.com/equa/?skip=0&limit=100')
    x = x.json()
    x = x["result"]
    
    func_list = []
    equa_list = []
    for data in x:
        func_list.append(data['function'])
        equa_list.append(data['equation'])
    func_list = func_list[::-1]
    equa_list = equa_list[::-1]
    merge_list = [func_list, equa_list]
    a = np.array(merge_list)
    a = np.transpose(a)
    df = pd.DataFrame(
        a,
        columns=(['Function', 'Equation'])
    )
    st.table(df)
    
def get_and_send(function, equation):
    login_url = 'https://numer-api-db.herokuapp.com/equa/login'
    login_body = {
        "email": "plug@example.com",
        "password": "123"
    }
    
    key = requests.post(url = login_url, json=login_body)
    # print(key.text[17:-2])
    token = key.text[17:-2]
    add_url = 'https://numer-api-db.herokuapp.com/equa/create'
    
    add_body = {
        "parameter": {
            "id": 0,
            "function": function,
            "equation": equation
        }
    }
    
    auth_token=token
    hed = {'Authorization': 'Bearer ' + auth_token}
    
    r = requests.post(
        url = add_url, 
        json=add_body, 
        headers=hed
        )
    
    # print(r.json())