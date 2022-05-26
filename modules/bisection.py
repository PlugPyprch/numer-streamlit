"""Bisection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kXMkhwDZlIbbIjcBWogfPkm_OjHcoIRJ
"""

# 
# 

from math import e
from math import sqrt
import sympy as sy
error_list = []
formula = "" #(x**6)-20

def compute(formula, **kwargs):
    expr = sy.sympify(formula)
    return expr.evalf(subs=kwargs)

def root(n, r=4):
  from numpy import roots
  return roots([1]+[0]*(r-1)+[-n])

def funcBi(x):
  ###### Code Here ###### 
  #x=x,formula="(x**6)-20"
  
  return compute(x=x,formula=formula)
  #######################

def checkZero(L, R):
  if (funcBi(L))*(funcBi(R)) < 0:
    return True
  else:
    return False

def main(xL=1.5, xR=2.0, Ep=0.000001):
  #xL = input(print('enter XL : '))
  xL = float(xL)
  #xR = input(print('enter XR : '))
  xR = float(xR)
  #Ep = input(print('enter Epsilon : '))
  Ep = float(Ep)

  if(checkZero(xL, xR)):
    i = 0
    while(True):
      xM = (xL + xR)/2
      i = i + 1
      if(funcBi(xM)*(funcBi(xR))) == 0:
        #print('-----Finish-----')
        #print('Iteration : ', i)
        #print('Error : ', Ec)
        error_list.append(Ec)
        #print('xS : ', xM)
        #print('-----Finish-----')
        break
      elif (funcBi(xM)*(funcBi(xR))) < 0:
        xL = xM
        xS = xM
        Ec = abs((xS - xR) / xS)
      elif (funcBi(xM)*(funcBi(xR))) > 0:
        xR = xM
        xS = xM
        Ec = abs((xS - xL) / xS)
      #print('xS : ', xS)
      #print('Iteration : ', i)
      #print('Error : ', Ec)
      error_list.append(Ec)
      if (Ec < Ep):
        #print('-----Finish-----')
        #print('Iteration : ', i)
        #print('Error : ', Ec)
        error_list.append(Ec)
        #print('xS : ', xM)
        #print('-----Finish-----')
        break