class Parser:
	cluster = [] # Stores inserted parsers. It's used in process_cluter

	def __init__(self, name, alias, description, argument_name='expression', argument_description='Mathematical expression'):
		self.name = name
		self.alias = alias
		self.description = description
		self.argument_name = argument_name
		self.argument_description = argument_description

	@staticmethod
	def process_cluster(args):
		"""
		Returns the expression parameter of the executed parser

		Parameters:
			args (Namespace): The parameter value of the executed parser.

		Returns:
			expression_operator (str, str): The mathematical expression and operator name of the parser.
		"""
		for parser in Parser.cluster:
			expression = parser.process(args)

			if expression != None:
				return expression

		return None

	def process(self, args):
		"""
		Returns the expression parameter of the parser in case the args corresponds with it.

		Parameters:
			args (Namespace): The parameter value of the executed parser.

		Returns:
			expression_operator (str, str): The mathematical expression and operator name of the parser.
		"""
		expression_is_provided = args.expression != None
		from_current_parser = args.which == self.name	

		if expression_is_provided and from_current_parser:
			expression = " ".join(args.expression)
			expression_operator = (expression, self.name)

			return expression_operator
		
		return None

	def insert_in(self, subparser):
		"""
		Inserts the current parser into the given subparser.
		"""
		new_parser = subparser.add_parser(self.name, aliases=[self.alias], help=self.description)
		new_parser.add_argument(self.argument_name, nargs='+', help=self.argument_description)
		new_parser.add_argument("--file", "-f", nargs='?', help="Save the operation and result of the calculation in a file", const='results', type=str)
		new_parser.set_defaults(which = self.name)
		
		Parser.cluster.append(self)
		return self
	
