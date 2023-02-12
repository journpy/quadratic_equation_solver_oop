# Import math and complex math libraries
# Also import the module containing codes that returns the discriminant

import math
import cmath
import the_quadratic_discriminant
from vertex import the_vertex		

def quadratic_formula():
	"""Model the quadratic formula"""
	while True:
		print("Enter 'q' at anytime to quit ")
		
		a = input('Enter a (quadratic term): ')
		if a == 'q':
			break

		b = input('Enter b (linear term): ')
		if b == 'q':
			break

		c = input('Enter c (constant term): ')
		if c == 'q':
			break

		#Handle errors from user input and continue executing program
		try:
			a = float(a)
			b = float(b)
			c = float(c)
	
			# Calculate vertex and axis of symmetry
			v = the_vertex(a, b, c)

			#if the discriminant is non-negative, it will have real roots and 
				# will require python's math library
			d = the_quadratic_discriminant.discriminant(a, b, c)

			if d >= 0:
				x_1 = (-b + math.sqrt(d))/(2*a)
				x_2 = (-b - math.sqrt(d))/(2*a)


			#if discriminant is negative, it will have complex roots and will 
				# require python's complex math library
			else:
				x_1 = (-b + cmath.sqrt(d))/(2*a)
				x_2 = (-b - cmath.sqrt(d))/(2*a)

			print(f"\nThe roots are {x_1} and {x_2}")
			print(f"\nDiscriminant: {d}\nVertex: {v}\n" 
					f"Axis of Symmetry: x = {v[0]}\n")

		except (ValueError, ArithmeticError):
			print("\nNot a quadratic equation!\n")
			continue




