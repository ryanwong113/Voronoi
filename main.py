from Fortune import Fortune
from Plane import Plane
from Point import Point
from Site import Site

def main():
	width = 10
	height = 10
	step_size = 0.1
	sites = [Site(2, 3), Site(5, 1)]
	plane = Plane(width, height, step_size, sites)
	fortune = Fortune(plane)

	fortune.run()

if __name__ == '__main__':
	main()