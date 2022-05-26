from modules import gauss_elimination
import streamlit as st
import numpy as np 
import pandas as pd
from history import get_and_send

def useGaussElimination():
    st.markdown("<h1 style='text-align: center; color: grey;'>Gauss Elimination</h1>", unsafe_allow_html=True)
    formula = st.text_input(label='Insert Formula')
    N = st.number_input(label='Enter number of unknowns', min_value=0, max_value=10, step=1)
    input_list = []
    for i in range(N*4):
        x = st.number_input(label='Insert input {}'.format(i+1), format="%.2f")
        input_list.append(x)
    
    if st.button('Compute'):
        if formula == '':
            st.write("Please Enter Formula!!!")
        else:
            get_and_send('Gauss Elimination', formula)
            gauss_elimination.main(N, input_list)
    