from sympy import symbols, sympify
from helpers.generate_function import to_pydef_str

def operate(latex): 
  x = symbols ('x')
  py_lambda_expr = to_pydef_str(latex)
  expr = py_lambda_expr.split(": ")[1]
  expr_value = sympify(expr).subs(x, x)

  return expr_value
