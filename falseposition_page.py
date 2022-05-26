from modules import falseposition
import streamlit as st
import numpy as np 
import pandas as pd
from history import get_and_send

def useFalsePosition():
    st.markdown("<h1 style='text-align: center; color: grey;'>False Position</h1>", unsafe_allow_html=True)
    formula = st.text_input(label='Insert Formula')
    x0 = st.number_input(label='Insert x0', format="%.2f")
    x1 = st.number_input(label='Insert x1', format="%.2f")
    Ep = st.number_input(label='Insert Epsilon', format="%.6f", step=0.000001)
    
    if st.button('Compute'):
        if formula == '':
            st.write("Please Enter Formula!!!")
        else:
            get_and_send('False Position', formula)
            falseposition.formula = formula
            falseposition.main(x0=x0,x1=x1,e=Ep)
            print(falseposition.error_list)
            arr = np.asarray(falseposition.error_list)
            falseposition.error_list = []
            chart_data = pd.DataFrame(
                arr
                ,
                columns=['Epsilon'])

            st.line_chart(chart_data)
            st.table(chart_data)