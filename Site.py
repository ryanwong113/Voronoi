# Site
from Point import Point

class Site:
	def __init__(self, x, y):
		self.point = Point(x, y)
		self.parabolas = {}