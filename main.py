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

"""
```
sum 4 + 4
python3 main.py sum 4 4
python3 main.py rest 4 4
python3 main.py mult 4 4
python3 main.py derivative \frac{1}{2}x-3
python3 main.py integral 4 4 x^2
```
"""
try:
	expression = sys.argv[1:][0]
	# TODO: Create an instance of calculator to test sum, rest...
	
	
except Exception as e:
	print("Debe ingresar la expresión como argumento")
