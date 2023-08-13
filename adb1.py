#!/usr/bin/env python3

from ppadb.client import Client
import numpy
import time
from mss import mss

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]
print('Connected device:', device.serial)

# Calculate middle coordinates
middle_x = 250
middle_y = 500

# Tap at the calculated middle coordinates
device.shell('input tap {} {}'.format(middle_x, middle_y))
