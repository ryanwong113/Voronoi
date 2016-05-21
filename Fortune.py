# Fortune's algorithm
import util
from Point import Point

class Fortune:
	# plane is a Plane object
	def __init__(self, plane):
		self.plane = plane
		self.step_size = plane.step_size
		self.sites = plane.sites
		self.scanned_sites = []
		self.sweep_line = []
		self.beach_line = [Point(x, 0) for x in util.frange(0, self.plane.width, self.step_size)]
		self.beach_line_by_sites = dict()

	def run(self):
		for level in util.frange(0, self.plane.height, self.step_size):
			# Sweep line
			sweep_line = self.build_sweep_line(level)

			# Encounter a site event
			if self.site_event():



			# TODO: Not sure it works properly or not
			if (level > self.sites[0].point.y):
				site = self.sites.pop(0)
				self.scanned_sites.append(site)

			# Build parabola for each of the scanned sites
			for site in self.scanned_sites:
				site.parabolas[level] = self.build_parabola(site, sweep_line)


	def site_event(self, sweep_line):



	def build_sweep_line(self, level):
		return [Point(x, level) for x in util.frange(0, self.plane.width, self.step_size)]

	def build_beach_line(self, site, index, parabola_point):
		
		if (parabola_point.y >= self.beach_line[index].y):
			if (parabola_point.y > self.beach_line[index].y):
				self.beach_line[index] = parabola_point

			if site in self.beach_line_by_sites:
				self.beach_line_by_sites[site].append(parabola_point)
			else:
				self.beach_line_by_sites[site] = [parabola_point]

	def build_parabola(self, site, sweep_line):
		parabola = []
		for index, sweep_line_point in enumerate(sweep_line):
			parabola_point = self.find_parabola_point(site.point, sweep_line_point)
			parabola.append(parabola_point)
			self.build_beach_line(site, index, parabola_point)
		return parabola

	def find_parabola_point(self, point, sweep_line_point):
		return Point(sweep_line_point.x, -0.5 * (((sweep_line_point.x-point.x)**2/(sweep_line_point.y-point.y)) - (sweep_line_point.y+point.y)))