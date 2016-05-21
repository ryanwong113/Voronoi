from Point import Point
import math

def euclidean_distance(a, b):
	return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def distance(a, b):
	return euclidean_distance(a, b)