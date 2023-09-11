from graham import *
import numpy as np
import math

def TSP(points: list):
	print('\n1. founded a convex hull:\n')
	points_on_convex_hull = find_convex_hull(points)
	points_in_convex_hull = list(set(points).difference(points_on_convex_hull))

	points_sorted = points_on_convex_hull.copy()
	for p_in in points_in_convex_hull:
		min_dist = math.inf
		min_i = None
		for i in range(-1, len(points_sorted) - 1):
			p_on_1, p_on_2 = points_sorted[i], points_sorted[i + 1]
			dist = distance(p_on_1, p_in) + distance(p_on_2, p_in)
			if dist < min_dist:
				min_i = i
				min_dist = dist
		if min_i == -1: 
			points_sorted.append(p_in)
		else: 
			points_sorted.insert(min_i + 1, p_in)
			# points_sorted[:min_i + 1] + [p_in] + points_sorted[min_i + 1:]

	return points_sorted

				


if __name__ == "__main__":
	
	inputs = [
		(2, 0),
		(0, 5),  
		(1, 1), 
		(6, 5),
		(0, 0), 
		(1, 2), 
		(6, 1), 
		(3, 4)
	]

	points = [Point(x, y) for (x, y) in inputs] 

	tour = TSP(points)
	print('\n2. founded a tour using nearest neighbor algorythm:\n')
	for p in tour:
		print("(" + str(p.x) + ", " + str(p.y) + ")\n")

	print('\n3. tour edges lines:\n')
	for i in range(len(tour) - 1):
		find_line(tour[i], tour[i + 1])
	find_line(tour[-1], tour[0])