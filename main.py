import sys
import argparse
from helpers.parser import Parser
from helpers.generate_function import generate_function
from operators.integral import integrate

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

	expression = Parser.process_c luster(args)

	# Process integral operation.
	if expression[1] == "integral":
		parts = expression[0].split(" ")
		a = float(parts[0])
		b = float(parts[1])
		math_function = parts[2]

		function = generate_function(math_function)
    
		result = integrate(a, b, function)

		print(result)

except Exception as e:
  print(e)
  print("Debe ingresar la expresión como argumento")
