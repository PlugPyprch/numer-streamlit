from modules import bisection
import streamlit as st
import numpy as np 
import pandas as pd
from history import get_and_send

def useBisection():
    st.markdown("<h1 style='text-align: center; color: grey;'>Bisection</h1>", unsafe_allow_html=True)
    formula = st.text_input(label='Insert Formula')
    xL = st.number_input(label='Insert xL', format="%.2f")
    xR = st.number_input(label='Insert xR', format="%.2f")
    Ep = st.number_input(label='Insert Epsilon', format="%.6f", step=0.000001)

    if st.button('Compute'):
        if formula == '':
            st.write("Please Enter Formula!!!")
        else:
            get_and_send('Bisection', formula)
            bisection.formula = formula #(x**6)-20
            bisection.main(xL=xL, xR=xR, Ep=Ep)
            print(bisection.error_list)
            arr = np.asarray(bisection.error_list)
            bisection.error_list = []
            chart_data = pd.DataFrame(
                arr
                ,
                columns=['Epsilon'])

            st.line_chart(chart_data)
            st.table(chart_data)