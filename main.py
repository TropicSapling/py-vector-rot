import math
import numpy as np
import matplotlib.pyplot as plt

from time import sleep

vector = np.array([5, 0])

v = math.radians(float(input("Rotation in degrees: ")))
count = int(input("Amount of times to rotate: "))

the_matrix = np.array([[math.cos(v), -math.sin(v)], [math.sin(v), math.cos(v)]])

rotated_vector = vector
for _ in range(count):
	plt.clf()
	plt.xlim(-10, 10)
	plt.ylim(-10, 10)
	
	rotated_vector = the_matrix.dot(rotated_vector)
	
	plt.quiver([0, 0], [0, 0], [vector[0], rotated_vector[0]], [vector[1], rotated_vector[1]], color=['r', 'g'], angles='xy', scale_units='xy', scale=1)
	
	plt.annotate('original vector', xy=(vector[0] + 0.5, vector[1] - 0.25))
	plt.annotate('rotated vector', xy=(rotated_vector[0] + 0.5, rotated_vector[1] - 0.25))
	
	plt.pause(0.25)
	
plt.show()