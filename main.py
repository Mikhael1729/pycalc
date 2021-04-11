import sys
import argparse
from helpers.parser import Parser
from helpers.generate_function import generate_function
from operators.integral import integrate
from operators.derivative import derivate
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

	operate = Parser("operate", "o", "Calculate a polynomial or constant function").insert_in(subparser)
	derivative = Parser("derivative", "d", "Calculate the derivative of a polynomial or constant function").insert_in(subparser)
	integral = Parser("integral", "i", "Calculate the definite integral of a polynomial or constant function").insert_in(subparser)
  
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
			ResultFile(args.file, "Integral Operation", steps, round(result, 4)).save_operation(False)

	elif operation == "derivative":
		parts = expression.split(" ")
		a = float(parts[0])
		math_function = "".join(parts[1:])

		result, steps = derivate(math_function, a)

		print(round(result, 4))

		if args.file != None:
			ResultFile(args.file, "Derivative Operation", steps, round(result, 4)).save_operation()

	elif operation == "operate":
		pass
	else:
		pass

except Exception as e:
  print(e)
  print("Debe ingresar la expresión como argumento")
