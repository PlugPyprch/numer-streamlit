import sympy as sy
formula = "" # x**3 - 5*x - 9
error_list = []

def compute(formula, **kwargs):
    expr = sy.sympify(formula)
    return expr.evalf(subs=kwargs)

def f(x):
    return compute(x=x,formula=formula)

# Implementing Secant Method

def secant(x0,x1,e,N):
    # print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            # print('Divide by zero error!')
            break
        
        x2 = float(x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) )) 
        error_list.append(x2)
        # print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            # print('Not Convergent!')
            break
        
        condition = abs(f(x2)) > e
    # print('\n Required root is: %0.8f' % x2)


# Input Section
# x0 = input('Enter First Guess: ')
# x1 = input('Enter Second Guess: ')
# e = input('Tolerable Error: ')
# N = input('Maximum Step: ')

def main(x0=2, x1=3, e=0.000001, N=10):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)
    N = int(N)
    secant(x0,x1,e,N)