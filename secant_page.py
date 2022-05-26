from modules import secant
import streamlit as st
import numpy as np 
import pandas as pd
from history import get_and_send

def useSecant():
    st.markdown("<h1 style='text-align: center; color: grey;'>Secant</h1>", unsafe_allow_html=True)
    formula = st.text_input(label='Insert Formula')
    x0 = st.number_input(label='Insert x0', format="%.2f")
    x1 = st.number_input(label='Insert x1', format="%.2f")
    Ep = st.number_input(label='Insert Epsilon', format="%.6f", step=0.000001)
    N = st.number_input(label='Insert Maximum Step', min_value=0, max_value=10, step=1)

    if st.button('Compute'):
        if formula == '':
            st.write("Please Enter Formula!!!")
        else:
            get_and_send('Secant', formula)
            secant.formula = formula 
            secant.main(x0=x0,x1=x1,e=Ep,N=N)
            print(secant.error_list)
            arr = np.asarray(secant.error_list)
            secant.error_list = []
            chart_data = pd.DataFrame(
                arr
                ,
                columns=['Epsilon'])

            st.line_chart(chart_data)
            st.table(chart_data)