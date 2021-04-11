from sympy import symbols, Eq, solve, sympify
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy.abc import x

def operate(): 
    x = symbols ('x')
    expression = '4x + 2x'
    expr_value = sympify(expression).subs(x, x)
    print(expr_value)

   