from math import *

# def f(x):
  # return ((sin(3*x))**3)/((2*x**5)**(1/3)) #Insert function manually

def integrate(a, b, f): #Integration function
  N = 1000000 #Number of times the sum will be made (1 million)
  value = 0
  result = 0

  for n in range(1, N + 1):
    """
    Aproximates area under a function using Riemann's sum (Midpoint rule)
    """
    value += f(a + (n - (1 / 2)) * ((b-a) / N))
  result = ((b - a) / N) * value
  return result
