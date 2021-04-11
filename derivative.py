from math import *

def f(x):
    return (3*x**5)/((2*x**4)**(1/3)) #Insert function manually

def derive(): #Differentiation function
    h = 0.00000000001 #Simulates limit when h approaches 0
    a = float(input("Insert value for x:")) #Point in which x=a
    numerator = f(a + h) - f(a)
    denominator = h
    derivative = numerator / denominator
    return float("%.3f" % derivative)

"""
derive() only calculates the derivative of a function when x = a.
It does not return algebraic expressions.
"""