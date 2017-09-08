import numpy as np
import matplotlib.pyplot as plt


loc_matrix = np.load("loc_matrix.npy")

print(loc_matrix[2])

plt.imshow(loc_matrix[2])