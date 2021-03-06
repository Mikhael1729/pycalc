from typing import Callable
import Algorithmia

"""
Converts a LaTex string into a Python function string.
"""
def to_pydef_str(expression):
	input = expression
	client = Algorithmia.client('sim7K6mfIVuU1NOVV6Kf+czVpDH1')
	algo = client.algo('Jeffro/LatexLambda/1.1.2')
	algo.set_options(timeout=300) # optional

	str_def = algo.pipe(input).result['func']

	return str_def

"""
Converts a LaTex string into a Python function.
"""
def generate_function(expression: str, debug=False) -> Callable[[int], str]:
	str_def = to_pydef_str(expression)
  #str_def = str_def.replace("e",2.7182818284590452353602874713526624977572470936999)
	if debug:
		print(str_def)

	f = eval(str_def)

	return f

