import serial
ser = serial.Serial('/dev/ttyUSB1' ,9600)
while 1:
    if(ser.in_waiting >0):
        line = ser.readline()
        print(line)