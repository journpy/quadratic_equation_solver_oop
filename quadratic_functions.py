import math
import cmath
import matplotlib.pyplot as plt
import numpy as np


class QuadraticFunctions:
	"""Model Quadratic Functions."""
	def __init__(self, a, b, c):
		""" Initialise attributes of quadratic functions"""
		self.a = a
		self.b = b
		self.c = c

	def convert_to_float(self):
		""" Return float values of user input"""
		self.a = float(self.a)
		self.b = float(self.b)
		self.c = float(self.c)
		return self.a, self.b, self.c


	def vertex(self):
		"""Return Tuple containing the vertex of the quadratic function"""
		qf = QuadraticFunctions(self.a, self.b, self.c)
		qf.convert_to_float()
		x = (-self.b) / (2*self.a)
		y = self.a*(x**2) + (self.b*x) + self.c
		ordered_pair = (x, y)
		return ordered_pair


	def discriminant(self):
		"""Return the value of the discriminant"""
		qf = QuadraticFunctions(self.a, self.b, self.c)
		qf.convert_to_float()
		quadratic_discriminant = (self.b**2) - (4*self.a*self.c)
		return quadratic_discriminant


	def quadratic_formula(self):
		"""Model the quadratic formula"""
		qf = QuadraticFunctions(self.a, self.b, self.c)
		v = qf.vertex()
		d = qf.discriminant()

		# If the discriminant is non-negative, it will have real roots and 
			# will require python's math library.
		if d >= 0:
			x_1 = (-self.b + math.sqrt(d))/(2*self.a)
			x_2 = (-self.b - math.sqrt(d))/(2*self.a)

		# If discriminant is negative, it will have complex roots and will 
			# require python's complex math library.
		else:
			x_1 = (-self.b + cmath.sqrt(d))/(2*self.a)
			x_2 = (-self.b - cmath.sqrt(d))/(2*self.a)

		print(f"\nThe roots are {x_1} and {x_2}\nDiscriminant: "
			f"{d}\nVertex: {v}\nAxis of Symmetry: x = {v[0]}\n")


	def style_graph(self):
		"""Style the graph"""
		plt.style.use("grayscale")
		plt.xlabel('x', loc='right', c='r')
		plt.ylabel('y', loc='top', c='r')
		plt.grid(True, linestyle=':')
		plt.title(f"Graph of ${self.a}x^2 + {self.b}x + {self.c}$", 
			fontsize=16, c='r')


	def plot_and_display_graph(self):
		"""Plot and display graph of the quadratic function."""
		x = np.linspace(-10, 10, 50)
		y = (self.a*(x)**2) + (self.b*x) + self.c

		qf = QuadraticFunctions(self.a, self.b, self.c)
		qf.style_graph()

		show_roots = np.roots([self.a, self.b, self.c])
		show_x_values = [show_roots[0], show_roots[1]]
		show_y_values = [0, 0]
		plt.scatter(show_x_values, show_y_values, s=100, c='r', 
				alpha=1, label='roots')
		plt.legend()
		plt.plot(x, y, 'b', linewidth=3)
		plt.show()


