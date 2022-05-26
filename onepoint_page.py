from modules import onepoint
import streamlit as st
import numpy as np 
import pandas as pd
from history import get_and_send

def useOnePoint():
    st.markdown("<h1 style='text-align: center; color: grey;'>One Point Iteration</h1>", unsafe_allow_html=True)
    formula = st.text_input(label='Insert Formula')
    x0 = st.number_input(label='Insert x0', format="%.2f")
    Ep = st.number_input(label='Insert Epsilon', format="%.6f", step=0.000001)

    if st.button('Compute'):
        if formula == '':
            st.write("Please Enter Formula!!!")
        else:
            get_and_send('One Point Iteration', formula)
            onepoint.formula = formula
            onepoint.main(x0=x0, Ep=Ep)
            print(onepoint.error_list)
            arr = np.asarray(onepoint.error_list)
            onepoint.error_list = []
            chart_data = pd.DataFrame(
                arr
                ,
                columns=['Epsilon'])

            st.line_chart(chart_data)
            st.table(chart_data)