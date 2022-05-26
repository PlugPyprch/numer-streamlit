
import streamlit as st
import numpy as np 
import pandas as pd
from history import get_and_send

def useLagrange():
    st.markdown("<h1 style='text-align: center; color: grey;'>Lagrange</h1>", unsafe_allow_html=True)
    formula = st.text_input(label='Insert Formula')

    if st.button('Compute'):
        if formula == '':
            st.write("Please Enter Formula!!!")
        else:
            get_and_send('Lagrange', formula)