from math import *

# def f(x):
    # return x**2 #Insert function manually

# def derive(): #Differentiation function
    # h = 0 #Simulates limit when h approaches 0
    # a = float(input("Insert value for x:")) #Point in which x=a
    # numerator = f(a + h) - f(a)
    # denominator = h
    # derivative = numerator / denominator
    # return float("%.3f" % derivative)

def derivate(f, a):
	h = 0.00000000001
	numerator = f(a + h) - f(a)
	denominator = h
	derivative = numerator / denominator
	return float("%.3f" % derivative)

"""
derive() only calculates the derivative of a function when x = a.
It does not return algebraic expressions.
"""
