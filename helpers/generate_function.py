from typing import Callable
import Algorithmia

"""
Converts a LaTex string into a Python function.
"""
def generate_function(expression: str, debug=False) -> Callable[[int], str]:
	input = expression
	client = Algorithmia.client('sim7K6mfIVuU1NOVV6Kf+czVpDH1')
	algo = client.algo('Jeffro/LatexLambda/1.1.2')
	algo.set_options(timeout=300) # optional

	str_def = algo.pipe(input).result['func']

	if debug:
		print(str_def)

	f = eval(str_def)

	return f
