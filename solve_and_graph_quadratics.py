from quadratic_functions import QuadraticFunctions

class SolveAndGraphQuadratics(QuadraticFunctions):
	"""Inherits from the parent class QuadraticFunctions."""


	def __init__(self, a, b, c):
		"""Initialise attributes of the parent class."""
		super().__init__(a, b, c)


	def main_loop(self):
		"""Main loop of the program"""
		while True:
			print("\nEnter 'q' at anytime to quit.\nStandard form of quadratic "
					"equation is ax^2 + bx + c = 0.\n")
			self.a = input('Enter a : ')
			if self.a == 'q' or self.a == 'Q':
				break
			self.b = input('Enter b : ')
			if self.b == 'q' or self.b == 'Q':
				break
			self.c = input('Enter c : ')
			if self.c == 'q' or self.c == 'Q':
				break

			try: 
				sgq = SolveAndGraphQuadratics(self.a, self.b, self.c)
				sgq.convert_to_float()
				sgq.quadratic_formula()
				sgq.plot_and_display_graph()
			except (ValueError, ArithmeticError):
				print("\nNot a quadratic equation!\n")
				continue
			
			




