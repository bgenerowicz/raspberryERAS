#!/usr/bin/env python
import sys
from time import time, clock
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.cluster import KMeans

def extract_data(scan_time,scan_increment):
    save_name = "data/data_" + str(scan_time) + "_" + str(scan_increment)
    fileObject = open(save_name, 'r')

    scan_time, scan_increment, loc_matrix = pickle.load(fileObject)

    loc_matrix[loc_matrix == 0] = 'nan'

    return scan_time, scan_increment, loc_matrix  #good: 180,185  216

# def make_plot(current_locations):
#     plt.axis([0, 800, 0, 480])
#     plt.gca().invert_yaxis()
#     plt.ion()
#
#     plt.plot(current_locations[:, 0], current_locations[:, 1], "*b")
#
# def add_mouse(centers):
#     plt.plot(centers[:, 0], centers[:, 1], "ro")

def plot_init():
    plt.axis([0, 800, 0, 480])
    plt.gca().invert_yaxis()
    plt.ion()

def cluster(current_locations,mice_number):
    kmeans = KMeans(n_clusters=mice_number, random_state=0).fit(current_locations)
    return kmeans.cluster_centers_


def remove_nans(itter_loc):
    # Find nans to remove them
    n = itter_loc.shape[0]

    #Remove from y
    ind = np.where(np.isnan(itter_loc[:, 1]))[0]
    final_locs = np.zeros((n - len(ind), 2))
    final_locs[:, 0] = np.delete(itter_loc[:, 0], ind)
    final_locs[:, 1] = np.delete(itter_loc[:, 1], ind)

    #Remove from x
    ind2 = np.where(np.isnan(final_locs[:, 0]))[0]
    final_locs2 = np.zeros((len(final_locs) - len(ind2), 2))
    final_locs2[:, 0] = np.delete(final_locs[:, 0], ind2)
    final_locs2[:, 1] = np.delete(final_locs[:, 1], ind2)

    return final_locs2

def main():
    n = 2 #Number of mice
    scan_time = 10.0
    scan_increment = 0.1

    scan_time, scan_increment, loc_matrix = extract_data(scan_time,scan_increment)

    plot_init()

    for j in range(0, loc_matrix.shape[0]):
        itter_loc = loc_matrix[j]

        current_locs = remove_nans(itter_loc)
        if len(current_locs) > 1:
            centers = cluster(current_locs,n)
            center_data = plt.scatter(centers[:, 0], centers[:, 1], s=500, color='red')


        paths = plt.scatter(itter_loc[:, 0], itter_loc[:, 1], s=100)
        current_seconds = "Time: %.2f out of %d (s)" % (scan_increment * (j + 1), scan_time)
        plt.title(current_seconds)
        plt.draw()
        # plt.pause(3)
        plt.pause(1e-2)
        paths.remove()
        if len(current_locs) > 1:
            center_data.remove()

        end = 1

    plt.show(block=True)



if __name__ == "__main__":
    main()