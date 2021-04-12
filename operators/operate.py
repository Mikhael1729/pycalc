from sympy import symbols, sympify, latex
from helpers.generate_function import to_pydef_str

def operate(latex_expr): 
  x = symbols ('x')
  py_lambda_expr = to_pydef_str(latex_expr)
  expr = py_lambda_expr.split(": ")[1]
  expr_value = sympify(expr).subs(x, x)
  
  return latex(expr_value)
