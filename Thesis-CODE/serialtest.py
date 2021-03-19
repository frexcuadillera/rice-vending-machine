#!/usr/bin/env python3
import serial
import time

device0 = '/dev/ttyUSB0'
device1 = '/dev/ttyUSB1'

ser = None


ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
ser.flush()
while True:
    ser.write(b"1")
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)