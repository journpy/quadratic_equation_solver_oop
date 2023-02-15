# Vertex of a quadratic function is at x = -b/2a

def vertex(a, b, c):
	"""Return Tuple containing the vertex of the quadratic function"""
	x = (-b) / (2*a)
	y = a*(x**2) + (b*x) + c

	ordered_pair = (x, y)
	return ordered_pair