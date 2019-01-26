import numpy as np
import matplotlib.pyplot as plt

the_matrix = np.matrix('1 2; 3 4')
vector = np.array([5, 5])
rotated_vector = np.array([-5, -5])

rot = float(input("Rotation in degrees: "))
count = int(input("Amount of times to rotate: "))

plt.quiver([0, 0], [0, 0], [vector[0], rotated_vector[0]], [vector[1], rotated_vector[1]], color=['r', 'g'], angles='xy', scale_units='xy', scale=1)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()