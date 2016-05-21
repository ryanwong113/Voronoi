# Utility class

# Find range with float step size
def frange(start, end=None, step=None):
	r = start
	while r < end:
		yield r
		r += step