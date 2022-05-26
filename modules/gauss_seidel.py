# Gauss Seidel Iteration
import sympy as sy
import streamlit as st
import numpy as np 
import pandas as pd
# Defining equations to be solved
# in diagonally dominant form
formula1 = ''
formula2 = ''
formula3 = ''

# x_list = []
# y_list = []
# z_list = []

all_list = []

def compute(formula, **kwargs):
    expr = sy.sympify(formula)
    return expr.evalf(subs=kwargs)

def f1(x,y,z):
    return compute(x=x, y=y, z=z, formula=formula1)

def f2(x,y,z):
    return compute(x=x, y=y, z=z, formula=formula2)

def f3(x,y,z):
    return compute(x=x, y=y, z=z, formula=formula3)

# f1 = lambda x,y,z: (17-y+2*z)/20
# f2 = lambda x,y,z: (-18-3*x+z)/20
# f3 = lambda x,y,z: (25-2*x+3*y)/20

# Initial setup
def main(e=0):
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1

    # Reading tolerable error
    # e = float(input('Enter tolerable error: '))

    # Implementation of Gauss Seidel Iteration
    # print('\nCount\tx\ty\tz\n')
    # st.markdown("<h1 color: red;'>Count    x    y    z", unsafe_allow_html=True)

    condition = True

    while condition:
        x_list = []
        
        x1 = f1(x0,y0,z0)
        y1 = f2(x1,y0,z0)
        z1 = f3(x1,y1,z0)
        # st.markdown("<h1 color: red;'>{:.2f}    {:.2f}    {:.2f}    {:.2f}</h1>".format(count,x1,y1,z1), unsafe_allow_html=True)
        # print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
        x_list.append(float(x1))
        x_list.append(float(y1))
        x_list.append(float(z1))
        all_list.append(x_list)
        # y_list.append(y1)
        # z_list.append(z1)
        
        e1 = abs(x0-x1);
        e2 = abs(y0-y1);
        e3 = abs(z0-z1);
        
        count += 1
        x0 = x1
        y0 = y1
        z0 = z1
        
        condition = e1>e and e2>e and e3>e
    # all_list.append(y_list)
    # all_list.append(z_list)

    # print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))
    st.markdown("<h2 color: red;'>Solution: x = {:.2f}, y = {:.2f} and z = {:.2f}</h2>".format(x1,y1,z1), unsafe_allow_html=True)
    # # print(gauss_seidel.all_list)
    # arr = np.asarray(all_list)
    # # print(arr)
    # all_list = []
    # chart_data = pd.DataFrame(
    #     arr
    #     ,
    #     columns=['x', 'y', 'z'])
    # st.table(chart_data)