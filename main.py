import sys
from Calculator import Calculator
from Calculator import User
from sympy import Symbol, cos

"""
Is the starting point of the program.

Handles the program execution. There two modes to use the app:

1. Passing only a expression as parameter.
2. Passing a file with LaTex code to calculate an expression

## Flags

`--file`: to save the calculations in an external file
"""
try:
	expression = sys.argv[1:][0]

	fernando = User("Fernando", "González", "1998-10-24 00:00:00")
	mikhael = User("Mikhael ", "Santos", "1998-10-24 00:00:00")

	x = Symbol('x')
	e = 1/cos(x)
	print(e.series(x, 0, 10))
	
except Exception as e:
	print("Debe ingresar la expresión como argumento")
