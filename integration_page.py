
import streamlit as st
import numpy as np 
import pandas as pd
from history import get_and_send

def useIntegration():
    st.markdown("<h1 style='text-align: center; color: grey;'>Integration</h1>", unsafe_allow_html=True)
    formula = st.text_input(label='Insert Formula')

    if st.button('Compute'):
        if formula == '':
            st.write("Please Enter Formula!!!")
        else:
            get_and_send('Integration', formula)