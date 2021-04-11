import sys
import argparse
from helpers.parser import Parser
from helpers.generate_function import generate_function

"""
Calculate polinomials operations and derivatives and integrals of them.

To see the options type: `python main.py --help`
"""
try:
	parser = argparse.ArgumentParser(description="P Y C A L C")
	parser.add_argument('--file', help='Store the operation in an external file', action='store_true', required=False)
	
	subparser = parser.add_subparsers(help="Available operations")

	operate = Parser("operate", "o", "Calculate a polynomial or constant function").insert_in(subparser)
	derivative = Parser("derivative", "d", "Calculate the derivative of a polynomial or constant function").insert_in(subparser)
	integral = Parser("integral", "i", "Calculate the definite integral of a polynomial or constant function").insert_in(subparser)

	args = parser.parse_args()

	expression = Parser.process_cluster(args)

	function = generate_function(expression[0], debug=True)
except Exception as e:
  print(e)
  print("Debe ingresar la expresión como argumento")
