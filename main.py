import sys
import argparse
from helpers.parser import Parser
from helpers.generate_function import generate_function, to_pydef_str
from operators.integral import integrate
from operators.derivative import derivate
from operators.operate import operate as operate_fun, numerical_operation
from models.ResultFile import ResultFile

"""
Calculate polinomials operations and derivatives and integrals of them.

To see the options type: `python main.py --help`
"""
try:
  # Create CLI interface.
  parser = argparse.ArgumentParser(description="P Y C A L C")
  parser.add_argument('--file', help='Store the operation in an external file', action='store_true', required=False)

  subparser = parser.add_subparsers(help="Available operations")

  operate = Parser("operate", "o", "Calculate a polynomial or constant function", argument_description="Mathematical expression. Format: [value] [expression]. Ej: operate 2 x^2").insert_in(subparser)
  derivative = Parser("derivative", "d", "Calculate the derivative of a polynomial or constant function", argument_description="Mathematical expression. Format: [value] [expression]. Ej: derivative 2 x^2").insert_in(subparser)
  integral = Parser("integral", "i", "Calculate the definite integral of a polynomial or constant function", argument_description="Mathematical expression. Format: [bottom] [top] [expression]. Ej: integral 0 2 x^2").insert_in(subparser)
  general = Parser("general", "g", "Calculate the given mathematical expression", argument_description="Mathematical expression. Format: [expression]. Ej: general 2x + x").insert_in(subparser)

  args = parser.parse_args()

  user_input = Parser.process_cluster(args)
  operation, expression = user_input[1], user_input[0]

  if operation == "integral":
    parts = expression.split(" ")
    a = float(parts[0]) # Lower bound of the definite integral
    b = float(parts[1]) # Upper bound of the definite integral.
    math_function = "".join(parts[2:])

    result, steps = integrate(a, b, math_function)

    print(round(result, 4))

    if args.file != None:
      ResultFile(args.file, "Integral Operation", steps, round(result, 4)).save_operation(False, latex_expression=math_function)

  elif operation == "derivative":
    parts = expression.split(" ")
    a = float(parts[0])
    math_function = "".join(parts[1:])

    result, steps = derivate(math_function, a)

    print(round(result, 4))

    if args.file != None:
      ResultFile(args.file, "Derivative Operation", steps, round(result, 4)).save_operation(latex_expression=math_function)

  elif operation == "operate":
    parts = expression.split(" ")
    a = float(parts[0])
    math_function = "".join(parts[1:])

    result, steps = numerical_operation(a, math_function)

    print(round(result, 4))

    if args.file != None:
      ResultFile(args.file, "Operate Numerically", steps, round(result, 4)).save_operation(latex_expression=math_function)

  elif operation == "general":
    result, steps = operate_fun(expression)

    print(result)

    if args.file != None:
      ResultFile(args.file, "Operate Operation", steps, result).save_operation(print_steps=False, latex_expression=expression)

  else:
    pass
except Exception as e:
  print(e)
  print("Error trying to calculate given expression. Remember to use \"\" for compound expressions")
