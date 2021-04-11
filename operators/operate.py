from sympy import symbols, Eq, solve, sympify
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy.abc import x

def operate(): 
    x, y = symbols ('x y')
    expression = '4x + 2x'
    expr_value = sympify(expression).subs(x, x)
    print(expr_value)
    
   