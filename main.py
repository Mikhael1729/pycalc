import sys
from Calculator import Calculator
# from sympy import Symbol, cos
import argparse
from integral import integrate

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
python3 main.py operate 24 + 2x            -- Only accepts expressions with no derivatives or integrals
python3 main.py derivative \frac{1}{2}x-3
python3 main.py integral 4 4 x^2
```
"""

try:
  # expression = sys.argv[1:]

  # parser = argparse.ArgumentParser(description="Pycalc — operations simplified")
  # subparser = parser.add_subparsers(help="Available options - help")

  # operate = subparser.add_parser('operate', aliases = ['o'], help = f'Compute a mathematical operation')
  # derivative = subparser.add_parser('derivative', aliases = ['d'], help = 'Compute the derivative of any expression')
  # integral = subparser.add_parser('integral', aliases = ['i'], help = 'Compute the definitive integral of any expression')

  # print(expression)
  # args = parser.parse_args(['derivative', '--help'])
  # print(args)

  # print(args.accumulate(args.integers))
  print(integrate(100, 0, 2))
except Exception as e:
  print(e)
  print("Debe ingresar la expresión como argumento")
