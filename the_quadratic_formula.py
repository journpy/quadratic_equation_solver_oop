# Import math and complex math libraries.
# Import modules containing codes that returns the discriminant and vertex.
import math
import cmath
from the_quadratic_discriminant import discriminant
from the_vertex import vertex		


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

	except (ValueError, ArithmeticError):
		print("\nNot a quadratic equation!\n")
		continue




