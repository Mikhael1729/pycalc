from math import sin, cos

def f(x):
  return sin(jj)

"""
TODO: Analyze, test and comment the code.
"""
def integrate(N, a, b):
  value = 0
  result = 0

  for n in range(1, N + 1):
    value += f(a + (n - (1 / 2)) * ((b-a) / N))
  
  result = ((b - a) / N) * value

  return result


