#!/usr/bin/env python

import evdev
import numpy as np
import os
import time
from threading import Thread
import pickle
import argparse

# Work out current path for save
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


#Parser used to take arguments
parser = argparse.ArgumentParser(description='Scan time | scan increment | save data')
parser.add_argument('integers', metavar='N', type=float, nargs='+',
                    help='Scan time | scan increment | save data')
args = parser.parse_args()
scan_time = args.integers[0]
scan_increment = args.integers[1]
save_data = args.integers[2]


#Making sure you pick the touchsceen
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
print("\ndevices:")
for q in devices:
	if q.name == "FT5406 memory based driver":
		device = evdev.InputDevice(q.fn)
	print(q.fn, q.name, q.phys)


#Update user
print("\npicked device:")
print(device)
print("\nscan time:")
print(int(args.integers[0]))
print("\nscan increment:")
print(args.integers[1])
print("\nsave?:")
if args.integers[2]:
	print("yes")
else:
	print("no")


time.sleep(5)



def read_touchscreen():
	#Variables
	global locations
	locations = np.zeros((10,2))
	finger = 0

	for event in device.read_loop():   #Read the device loop 
		if event.type == evdev.ecodes.EV_ABS:
			if event.code == evdev.ecodes.ABS_MT_SLOT:
				finger = event.value
			if event.code == evdev.ecodes.ABS_MT_POSITION_X:
	                                locations[finger,0] = event.value
			if event.code == evdev.ecodes.ABS_MT_POSITION_Y:
	                                locations[finger,1] = event.value
			if event.code == evdev.ecodes.ABS_MT_TRACKING_ID:
				if event.value == -1:
					locations[finger,0] = 0
					locations[finger,1] = 0

def update_location():
	prev_time = time.time()
	global itteration
	itteration = 0
	loc_matrix = np.zeros((int(scan_time/scan_increment),10,2))
	while 1:
		if ((time.time() - prev_time) > scan_increment):
			if (itteration*scan_increment < scan_time):
			    os.system('clear')
			    current_seconds = "time: %.2f out of %d (s)" % (scan_increment*(itteration+1),scan_time)
			    print(current_seconds)
			    print(locations)

			    loc_matrix[itteration] = locations
			    prev_time = time.time()
			    itteration += 1
			else:
				#Save the data
				if save_data == 1:
					save_name = "data/" + "data_" + str(scan_time) + "_" + str(scan_increment)
					saving_data = [scan_time,scan_increment,loc_matrix]
					fileObject = open(save_name,'w+')
					pickle.dump(saving_data,fileObject)
					fileObject.close()
					print("saved!")
				else:
					print("done!")
				# np.save("loc_matrix",loc_matrix)
				os._exit(1)


Thread(target = read_touchscreen).start()
Thread(target = update_location).start()