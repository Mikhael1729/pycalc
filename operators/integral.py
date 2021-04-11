from math import *
from helpers.generate_function import generate_function

# def f(x):
  # return ((sin(3*x))**3)/((2*x**5)**(1/3)) #Insert function manually

def integrate(a, b, math_function): #Integration function
  f = generate_function(math_function)
  N = 1000000 # Number of times the sum will be made (1 million)
  value = 0
  result = 0

  part = None
  for n in range(1, N + 1):
    """
    Aproximates area under a function using Riemann's sum (Midpoint rule)
    """
    part = a + (n - (1 / 2)) * ((b-a) / N)
    value += f(part)

  result = ((b - a) / N) * value

  steps = ''
  steps += str(math_function.replace('x', f'({str(round(part, 4))})')) + "\\\\"
  steps += '\\frac{{{0} - {1}}}{{{2}}}\\cdot{{3}}'.format(b, a, N, value) + "\\\\"

  return result, steps

