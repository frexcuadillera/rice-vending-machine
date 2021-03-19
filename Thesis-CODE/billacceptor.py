import serial
import os

#print(serial.__version__)

device0 = '/dev/ttyUSB0'
device1 = '/dev/ttyUSB1'

serialbuffer = 0
credit = 0
ser = None

try:
    ser = serial.Serial(device0, 9600)
except:
    try:
        ser = serial.Serial(device1, 9600)
    except Exception as ex:
        print(ex)

#ser.open()

while True:
    serialbuffer = ser.readline().decode("utf-8").lstrip().rstrip()

    credit += int(serialbuffer)
    #print(credit)
    
    g = open("/home/pi/Desktop/Thesis-CODE/pulses.txt", "w")
    g.write(str(credit))
    g.close()
    #os.environ['VENDING_MACHINE_CREDIT'] = str(credit)
    
    print(config('VENDING_MACHINE_CREDIT'))
    
    if(config('VENDING_MACHINE_CREDIT') == "0"):
        credit = 0
        int(credit)
        
    
    #int(credit)
    
    #pulses =  open("/home/pi/Desktop/Thesis-CODE/pulses.txt", "r")
    #data = pulses.read().replace('\n', '')
    
    #print(data)
    #//if(data == "0"):
    #//    credit = 0
        
    #pulses.close()
    

    
    
                