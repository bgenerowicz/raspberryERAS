import evdev
import numpy as np
import os
import time
from threading import Thread
import matplotlib.pyplot as plt


device = evdev.InputDevice('/dev/input/event0')
print(device)

def read_touchscreen():
	#Variables
	global locations
	locations = np.zeros((10,2))
	finger = 0

	for event in device.read_loop():
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
	itteration = 0
	while 1:
		if (time.time() - prev_time) > 1:
		    os.system('clear')
		    print(locations)
		    prev_time = time.time()

# def store_data():
# 	prev_time = time.time()
# 	while 1:
# 		if (time.time() - prev_time) > 5:
# 		    prev_time = time.time()
# 		    im = np.zeros((480,800))
# 		    plt.plot(im)
	# Let's make an image!
    # im = np.zeros((480,800))

#     for i in range(0,locations.shape[0]):
#     	im[locations[i,1], locations[i,0]] = 1

Thread(target = read_touchscreen).start()
Thread(target = update_location).start()
Thread(target = create_image).start()