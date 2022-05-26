from modules import gauss_seidel
import streamlit as st
import numpy as np 
import pandas as pd
from history import get_and_send

def useGaussSeidel():
    st.markdown("<h1 style='text-align: center; color: grey;'>Gauss Seidel</h1>", unsafe_allow_html=True)
    formula1 = st.text_input(label='Insert Formula1')
    formula2 = st.text_input(label='Insert Formula2')
    formula3 = st.text_input(label='Insert Formula3')
    Ep = st.number_input(label='Insert Epsilon', format="%.6f", step=0.000001)
    
    if st.button('Compute'):
        if formula1 == '':
            st.write("Please Enter Formula!!!")
        elif formula2 == '':
            st.write("Please Enter Formula!!!")
        elif formula3 == '':
            st.write("Please Enter Formula!!!")
        else:
            get_and_send('Gauss Seidel', formula1)
            get_and_send('Gauss Seidel', formula2)
            get_and_send('Gauss Seidel', formula3)
            gauss_seidel.formula1 = formula1
            gauss_seidel.formula2 = formula2
            gauss_seidel.formula3 = formula3
            gauss_seidel.main(e=Ep)
            # print(gauss_seidel.all_list)
            arr = np.asarray(gauss_seidel.all_list)
            # print(arr)
            gauss_seidel.all_list = []
            chart_data = pd.DataFrame(
                arr
                ,
                columns=['x', 'y', 'z'])
            st.table(chart_data)
            #st.markdown("<h2 color: red;'>Solution: x = {:.2f}, y = {:.2f} and z = {:.2f}</h2>".format(gauss_seidel.all_list[3][0],gauss_seidel.all_list[3][1],gauss_seidel.all_list[3][2]), unsafe_allow_html=True)