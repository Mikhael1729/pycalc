from math import *
from helpers.generate_function import generate_function

def derivate(math_function, a):
	"""
	derivate() only calculates the derivative of a function when x = a.
	It does not return algebraic expressions.
	"""
	f = generate_function(math_function)
	h = 0.00000000001
	numerator = f(a + h) - f(a)
	denominator = h
	derivative = numerator / denominator

	result = float("%.3f" % derivative)

	# Compute steps.
	delta_f = math_function.replace('x', f'({a} + {h})')
	value_f = math_function.replace('x', f'({a})')
	steps = '\\frac{{{0} - {1}}}{{{2}}}'.format(delta_f, value_f, h)

	return result, steps

