#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import time
import pickle

# Variables
scaling = 40
scroll_speed = 20


# loc_matrix = np.load("loc_matrix.npy")
scan_time = 50
scan_increment = 0.2
save_name = "data/data_" + str(scan_time) + "_" + str(scan_increment)
fileObject = open(save_name,'r')

scan_time,scan_increment,loc_matrix = pickle.load(fileObject)

print("total scan time: " + str(scan_time) + " seconds")
print("scan increment: " + str(scan_increment) + " seconds")

########
#Plot the locations itteratively
plt.axis([0,800,0,480])
plt.gca().invert_yaxis()
plt.ion()
loc_matrix[loc_matrix == 0] = 'nan'

for j in range(0,loc_matrix.shape[0]):
    itter_loc = loc_matrix[j]

    paths = plt.scatter(itter_loc[:,0], itter_loc[:,1], s = 100)

    current_seconds = "Time: %.2f out of %d (s)" % (scan_increment * (j + 1), scan_time)
    plt.title(current_seconds)
    plt.draw()
    # plt.pause(1e-6)
    plt.pause(1e-2)
    paths.remove()
    
    end = 1

plt.show(block=True)











###################
# Other approach using im_grid (slower)
# #Make grid
# im_grid = np.zeros((480/scaling,800/scaling))
#
#
#
# for j in range(0,loc_matrix.shape[0]):
#     locations = loc_matrix[j]/scaling
#
#     for i in range(0,locations.shape[0]):
#         if (locations[i,1] != 0) or (locations[i,0] != 0):
#             im_grid[locations[i, 1], locations[i, 0]] = 1
#
#
#
#
#     plt.imshow(im_grid)
#     current_seconds = "Time: %.2f out of %d (s)" % (scan_increment * (j + 1), scan_time)
#     plt.title(current_seconds)
#     plt.pause(scan_increment/scroll_speed)
#
#     plt.cla()
#
#
#
#
#     #Clear grid for new entries
#     im_grid = np.zeros((480/scaling,800/scaling))

# #Plot method
# for j in range(0,loc_matrix.shape[0]):
#     itter_loc = loc_matrix[j]
#     itter_loc[itter_loc == 0] = 'nan'
#     x = itter_loc[:,0]
#     y = itter_loc[:,1]
#
#     plt.scatter(x, y, s = 1000)
#     plt.axis([0,800,0,480])
#     current_seconds = "Time: %.2f out of %d (s)" % (scan_increment * (j + 1), scan_time)
#     plt.title(current_seconds)
#     plt.gca().invert_yaxis()
#     plt.pause(0.00001)
#     plt.cla()


# # #######################



