import math
import numpy as np
import matplotlib.pyplot as plt

from time import sleep

# Input
v = math.radians(float(input("Rotation in degrees: ")))
count = int(input("Amount of times to rotate: "))

# Definitions
vector = np.array([5, 0])
rotated_vector = vector
the_matrix = np.array([[math.cos(v), -math.sin(v)], [math.sin(v), math.cos(v)]])

# Rotate vector <count> times
for _ in range(count):
	# Reset
	plt.clf()
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	
	# Rotate vector
	rotated_vector = the_matrix.dot(rotated_vector) # Dot product of The Matrix and the vector, resulting in rotating the vector
	
	# Draw vectors
	plt.quiver([0, 0], [0, 0], [vector[0], rotated_vector[0]], [vector[1], rotated_vector[1]], color=['r', 'g'], angles='xy', scale_units='xy', scale=1)
	
	plt.annotate('original vector', xy=(vector[0] + 0.5, vector[1] - 0.25))
	plt.annotate('rotated vector', xy=(rotated_vector[0] + 0.5, rotated_vector[1] - 0.25))
	
	plt.pause(0.25)
	
plt.show()