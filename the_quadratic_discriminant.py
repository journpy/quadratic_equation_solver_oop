# Discriminant is b^2 - 4ac

def discriminant(first_term, second_term, third_term):
	"""Return the value of the discriminant"""
	first_term = float(first_term)
	second_term = float(second_term)
	third_term = float(third_term)

	quadratic_discriminant = (second_term**2) - (4*first_term*third_term)
	return quadratic_discriminant