# Save data e.g. site coordinates, area of the plane, step size...
import operator
from Site import Site

class Plane:
	def __init__(self, width, height, step_size, sites):
		self.width = width
		self.height = height
		self.step_size = step_size
		self.sites = sites

	# Sort all the sites by their y coordinates
	def sort_sites(self, sites):
		return sorted(sites, key=lambda site: site.point.y)

	def in_range(site):
		return site.point.x >= 0 and site.point.x <= width and site.point.y >= 0 and site.point.y <= height
