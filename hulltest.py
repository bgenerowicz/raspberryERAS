#!/usr/bin/env python
import sys
from time import time, clock
import numpy as np
import matplotlib.pyplot as plt
import pickle
#
#
#
# #######################
# result = [];
# f = open('test_data.dat');
# total_num = int(f.readline());
#
# # f = 100*np.random.rand(10,2)
# # total_num = 10
#
# while total_num != 0:
#     a = (f.readline().split())
#     a = (int(a[0]), int(a[1]))  # a[0] for X    a[1] for Y
#     result.append(a);
#     total_num -= 1;
#
# t = clock()
#
#
# def distance(p, q):
#     # distance between points p and q
#     dx, dy = int(q[0]) - int(p[0]), int(q[1]) - int(p[1])
#     return (dx * dx) + (dy * dy)
#
#
# def turn(p, q, r):
#     # returns -ve,0, or +ve depending on the angle p-q-r makes (with q being the angle)
#     return ((int(q[0]) - int(p[0])) * (int(r[1]) - int(p[1])) - (int(r[0]) - int(p[0])) * (int(q[1]) - int(p[1])) > int(
#         0)) - (
#            (int(q[0]) - int(p[0])) * (int(r[1]) - int(p[1])) - (int(r[0]) - int(p[0])) * (int(q[1]) - int(p[1])) < int(
#                0))
#
#
# L_turn, R_turn, straight = (1, -1, 0)
#
#
# def next_hull_point(points, p):
#     # outputs the next hull point
#     q = p
#     for r in points:
#         t = turn(p, q, r)
#         if t == R_turn or t == straight and distance(p, r) > distance(p, q):
#             q = r
#     return q
#
#
# def find_min_p(points):
#     min_num = points[0]
#     for i in points:
#         if int(i[1]) < int(min_num[1]):
#             min_num = i
#         elif int(i[1]) == int(min_num[1]):
#             if int(i[0]) < int(min_num[0]):
#                 min_num = i
#     return min_num
#
#
# def find_hull(points):
#     min_p = find_min_p(points);
#     hull = [min_p]
#     for p in hull:
#         q = next_hull_point(points, p)
#         if q != hull[0]:
#             hull.append(q)
#     return hull
#
#
# print (find_hull(result))  # points
# #
# # the real computing time should be after finish calculating the points
# # which is not include that index transction part so time counter should
# # put before the index transction part.
# #
# print ('CPU time: ', clock() - t)
#
#
# def hull_index(points, hull):
#     result = []
#     for i in hull:
#         result.append(points.index(i))
#     return result
#
#
# print (hull_index(result, find_hull(result)))  # index
#
# end = 1
#
#
#







###################





# import numpy as np
# import matplotlib.pyplot as plt
#
# # jarvis(S)
# #    pointOnHull = leftmost point in S
# #    i = 0
# #    repeat
# #       P[i] = pointOnHull
# #       endpoint = S[0]      // initial endpoint for a candidate edge on the hull
# #       for j from 1 to |S|
# #          if (endpoint == pointOnHull) or (S[j] is on left of line from P[i] to endpoint)
# #             endpoint = S[j]   // found greater left turn, update endpoint
# #       i = i+1
# #       pointOnHull = endpoint
# #    until endpoint == P[0]      // wrapped around to first hull point
#
# def hull_test(current_locations):
#     # x = current_locations[:, 0]
#     # y = current_locations[:, 1]
#     # n = current_locations.shape[0]
#     # hull = []
#     #
#     #
#     # x_left, idx = min((val, idx) for (idx, val) in enumerate(x))
#     #
#     # p0 = [x_left, y[idx]]  #Left most position
#     # hull.append(p0)
#     #
#     # for i in range(1,n):
#     #
#     #
#     #
#     #
#     # # plt.scatter(x, y)
#     # # plt.scatter(x_left,y[idx],color='red')
#     # # plt.show()
#
#     ##### new
#     x = current_locations[:, 0]
#     y = current_locations[:, 1]
#     n = current_locations.shape[0]
#     P = np.zeros((10,1))
#
#
#     x_left, idx = min((val, idx) for (idx, val) in enumerate(x))
#
#     pointOnHull = idx  #Left most position
#     # hull.append(pointOnHull)
#
#     while endpoint !=
#     for i in range(0, n):
#         P[i] = pointOnHull
#
#
#
#
#
#
#     print("1")
#
#
# # def calc_angle(p1,p2):
#
#
#
# test = np.random.rand(10,2)
#
# hull_test(test)

def orientation(p,q,r):
    val = (q[1]- p[1]) * (r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])

    if val > 0:
        # print("clockwise")
        return 1
    elif val == 0:
        # print("colinear")
        return 0
    else:
        # print("counterclockwise")
        return 2

def next_point(p,q,points,current_locations):

        # print("q = " + str(q))

    counter_count = 0
    for r in points:
        if (r != p) and (r != q):
            # print("r = " + str(r))
            temp = orientation(current_locations[p], current_locations[q], current_locations[r])
            if temp != 2:
                # print("error")
                return 0

            # If n-2 counts, then its the right one
            counter_count += 1
            if counter_count == (current_locations.shape[0] - 2):
                # print("q = " + str(q) + " is the best")
                return 1

def make_plots(current_locations,hull):

    plt.axis([0, 800, 0, 480])
    plt.gca().invert_yaxis()
    plt.ion()


    plt.plot(current_locations[:, 0], current_locations[:, 1], "*b")

    x = []
    y = []
    for i in hull:
        x.append(current_locations[i, 0])
        y.append(current_locations[i, 1])

    plt.plot(x,y,"r")
    plt.plot(x, y, "*r")
    plt.show(block='true')


def hull_test(current_locations):
    x = current_locations[:, 0]
    x_left, idx = min((val, idx) for (idx, val) in enumerate(x))
    # min_num = np.nanmin(x)
    # idx = x.tolist().index(min_num)

    leftpoint = idx
    points = range(0,current_locations.shape[0])

    hull = []
    hull.append(idx)

    p = leftpoint
    check_for_complete = []

    #Safety
    if current_locations.shape[0] < 3:
        print("no mouse")
        return 0
    else:
        print("good")

    while hull[0] != check_for_complete:
        for q in points:
            if (q != p):
                nxtp = next_point(p,q,points,current_locations)

                if nxtp:
                    check_for_complete = q
                    hull.append(q)
                    break
        p = q

    hull_locs = np.zeros((len(hull),2))
    for i in range(0,hull_locs.shape[0]):
        hull_locs[i] =  current_locations[hull[i]]

    return hull_locs
    # return hull

def radius_matrix(current_locations):
    n = current_locations.shape[0]
    r_matrix = np.zeros((n,n))

    for i in range(0,n):
        for j in range(0,n):
            if i != j:
                r_matrix[i,j] = np.sqrt((current_locations[i,1]-current_locations[j,1])**2 + (current_locations[i,0]-current_locations[j,0])**2)

    return r_matrix

def extract_data():
    # Variables
    scaling = 40
    scroll_speed = 20

    # loc_matrix = np.load("loc_matrix.npy")
    # scan_time = 50
    # scan_increment = 0.2
    scan_time = 5.0
    scan_increment = 1.0


    save_name = "data/data_" + str(scan_time) + "_" + str(scan_increment)
    fileObject = open(save_name, 'r')

    scan_time, scan_increment, loc_matrix = pickle.load(fileObject)

    end = 1
    return loc_matrix[1]  #good: 180,185

def determine_locations(current_locations,r_matrix,num_mice,max_length):
    #pseudocode:
    #- start on the left, look at nodes in range (up to 3 other nodes)
    #- exclude them all from the list
    #- start on other extreme and do the same
    #

    #Find most left point
    x = current_locations[:, 0]
    x_left, idx = min((val, idx) for (idx, val) in enumerate(x))

    #Total number of points (can't use the same point twice)
    n = r_matrix.shape[0]
    points = range(0,n)




    #Set positions > max_length in r_matrix to zeros, else 1
    for i in range(0,n):
        for j in range(0,n):
            if (r_matrix[i,j]>max_length):
                r_matrix[i, j] = np.nan
            else:
                r_matrix[i, j] = 1

    # # Make new locations based on points within range
    new_locs = np.zeros(current_locations.shape)
    new_locs[:,0] = r_matrix[idx, :] * current_locations[:,0]
    new_locs[:, 1] = r_matrix[idx, :] * current_locations[:, 1]

    #Find nans to remove them
    ind = np.where(np.isnan(new_locs[:,0]))[0]
    final_locs = np.zeros((n-len(ind), 2))
    final_locs[:,0] = np.delete(new_locs[:,0],ind)
    final_locs[:, 1] = np.delete(new_locs[:,1],ind)

    return final_locs
    # return new_locs
    # save_nans = []
    # for i in range(0,n):
    #     if new_locs[i,0] == 'nan':
    #         print("1")
    #         save_nans.append(i)


    # #hull?
    # hull = []
    # for i in range(0,n):
    #     if r_matrix[idx, i] == 1:
    #         hull.append(i)
    #
    # return hull

def make_basic_plot(current_locations):
    plt.axis([0, 800, 0, 480])
    plt.gca().invert_yaxis()
    plt.ion()

    plt.plot(current_locations[:, 0], current_locations[:, 1], "*b")

def make_hull_plots(hull_locs):
    x = hull_locs[:, 0]
    y = hull_locs[:, 1]

    plt.plot(x, y, "r")
    plt.plot(x, y, "*r")

# def make_hull_plots(current_locations,hull_locs):
#
#
#     plt.axis([0, 800, 0, 480])
#     plt.gca().invert_yaxis()
#     plt.ion()
#
#
#     plt.plot(current_locations[:, 0], current_locations[:, 1], "*b")
#
#     x = hull_locs[:,0]
#     y = hull_locs[:,1]
#
#     plt.plot(x,y,"r")
#     plt.plot(x, y, "*r")
#     plt.show(block='true')

def main():
    #Variables
    num_mice = 2
    max_length = 400


    # current_locations = np.random.rand(10, 2)
    # current_locations = np.zeros((6,2))
    # current_locations[0] = [10,10]
    # current_locations[1] = [15,5]
    # current_locations[2] = [20,15]
    # current_locations[3] = [30,15]
    # current_locations[4] = [15,20]
    # current_locations[5] = [15,10]


    current_locations = extract_data()
    r_matrix = radius_matrix(current_locations)

    # for i in range(0,num_mice):
    mice_locations = determine_locations(current_locations,r_matrix,num_mice,max_length)
    hull_locs = hull_test(mice_locations)


    # make_plots(current_locations, hull)
    if hull_locs.any():
        make_basic_plot(current_locations)
        make_hull_plots(hull_locs)
        plt.show(block='true')
    end = 1

if __name__ == "__main__":
    main()