import sys

try:
	expression = sys.argv[1:][0]
except Exception as e:
	print("Debe ingresar una expresión válida")
