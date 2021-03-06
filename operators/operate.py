from sympy import symbols, sympify, latex
from helpers.generate_function import to_pydef_str

def operate(latex_expr): 
  x = symbols ('x')
  py_lambda_expr = to_pydef_str(latex_expr)
  expr = py_lambda_expr.split(": ")[1]
  expr_value = sympify(expr).subs(x, x)

  result = latex(expr_value)
  steps = ''

  return result, steps

def numerical_operation(a, latex_expr):
  py_str_def = to_pydef_str(latex_expr)
  math_def = eval(py_str_def)
  result = math_def(a)

  steps = latex_expr.replace('x', f'({a})')

  return result, steps


