from streamlit_option_menu import option_menu
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import numpy as np 
import sympy as sy

from bisection_page import useBisection
from onepoint_page import useOnePoint
from falseposition_page import useFalsePosition
from newton_page import useNewtonRaphson
from secant_page import useSecant

from gauss_elimination_page import useGaussElimination
from gauss_seidel_page import useGaussSeidel
from cramer_page import useCarmer
from gauss_jordan import useGaussJordan
from jacobi_page import useJacobi

from newton_divide_page import useNewtonDivide
from lagrange_page import useLagrange
from spline_page import useSpline
from regression_page import useRegression
from integration_page import useIntegration
from differentiation_page import useDifferentiation

from history import history_main

html = """
<style>
    #MainMenu {visibility: hidden;}
    .css-gr05f0 {visibility: hidden;}
    .css-1adrfps {padding-top: 40px;}
    .css-6awftf {visibility: hidden;}
    .vega-embed summary {visibility: hidden;}
    .css-1qrvfrg {width: 270px}
    .css-qri22k {visibility: hidden;}
</style>
"""
st.markdown(html, unsafe_allow_html=True)


with st.sidebar:
    choose = option_menu("Numeric Function", ['Bisection', 'FalsePosition', 'OnePoint', 'Secant', 'Newton', "Cramer's Rule", 
                                            'GaussElimination', 'GaussSeidel', 'GaussJordan', 'Jacobi',
                                            "Newton's divided-differences", 'Lagrange', 'Spline', 
                                            'Regression', 
                                            'Integration', 
                                            'Differentiation',
                                            'History'],
                        icons=['infinity', 'infinity', 'infinity', 'infinity','infinity', 
                            'arrow-up-right', 'arrow-up-right', 'arrow-up-right', 'arrow-up-right', 'arrow-up-right',
                            'border-all', 'border-all', 'border-all',
                            'percent',
                            'percent',
                            'percent'],
                        menu_icon="app-indicator", default_index=0,
    #                      styles={
    #     "container": {"padding": "5!important", "background-color": "#fafafa"},
    #     "icon": {"color": "orange", "font-size": "25px"}, 
    #     "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    #     "nav-link-selected": {"background-color": "#02ab21"},
    # }
    )
    
if choose == 'Bisection':
    useBisection()
elif choose == 'OnePoint':
    useOnePoint()
elif choose == 'FalsePosition':
    useFalsePosition()
elif choose == 'Newton':
    useNewtonRaphson()
elif choose == 'Secant':
    useSecant()

elif choose == "Cramer's Rule":
    useCarmer()
elif choose == 'GaussElimination':
    useGaussElimination()
elif choose == 'GaussSeidel':
    useGaussSeidel()
elif choose == 'GaussJordan':
    useGaussJordan()
elif choose == 'Jacobi':
    useJacobi()
    
elif choose == "Newton's divided-differences":
    useNewtonDivide()
elif choose == 'Lagrange':
    useLagrange()
elif choose == 'Spline':
    useSpline()
elif choose == 'Regression':
    useRegression()
elif choose == 'Integration':
    useIntegration()
elif choose == 'Differentiation':
    useDifferentiation()
    
elif choose == 'History':
    history_main()




