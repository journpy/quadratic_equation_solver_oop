# Import math and complex math libraries.
import math
import cmath
# Import modules containing codes that returns the discriminant and vertex.
from the_quadratic_discriminant import discriminant
from the_vertex import vertex
# Import graphing packages	
import matplotlib.pyplot as plt
import numpy as np	


def show_messages():
	"""Display helpful messages."""
	quit_message = "Enter 'q' at anytime to quit."
	standard_form = "Standard form of quadratic equation is ax^2 + bx + c = 0."
	print(f"\n{quit_message}\n{standard_form}\n")


# Model the quadratic formula."""
while True:
	show_messages()

	a = input('Enter a : ')
	if a == 'q' or a == 'Q':
		break
	b = input('Enter b : ')
	if b == 'q' or b == 'Q':
		break
	c = input('Enter c : ')
	if c == 'q' or c == 'Q':
		break

	# Handle errors from user input and continue executing program.
	try:
		a, b, c = float(a), float(b), float(c)
	
		# Calculate vertex and discriminant
		v, d = vertex(a, b, c), discriminant(a, b, c)

		# If the discriminant is non-negative, it will have real roots and 
			# will require python's math library.
		if d >= 0:
			x_1, x_2 = (-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)

		# If discriminant is negative, it will have complex roots and will 
			# require python's complex math library.
		else:
			x_1, x_2 = (-b + cmath.sqrt(d))/(2*a), (-b - cmath.sqrt(d))/(2*a)

		print(f"\nThe roots are {x_1} and {x_2}\nDiscriminant: "
			f"{d}\nVertex: {v}\nAxis of Symmetry: x = {v[0]}\n")


		# Plot and display graph of the quadratic function
		plt.style.use("_classic_test_patch")

		# Array of 100 x values between -5 and 5
		x = np.linspace(-5, 5, 100)

		# Function to be graphed
		y = (a*(x)**2) + (b*x) + c

		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)

		# Title of graph
		plt.title(f"Graph of {a}x^2 + {b}x + {c}.", fontsize=12, fontweight='bold')

		# Set position and color of axes
		ax.spines['left'].set_position('center')
		ax.spines['bottom'].set_position('zero')
		ax.spines['left'].set_color('r')
		ax.spines['bottom'].set_color('b')
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		
		# Set position of ticks and show grids
		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
		ax.grid(True, linestyle=':', linewidth=2)
		
		# Display graph
		plt.plot(x, y, 'b')
		plt.show()


	except (ValueError, ArithmeticError):
		print("\nNot a quadratic equation!\n")
		continue




