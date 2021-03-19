import serial
import RPi.GPIO as GPIO
import time

#def bill():

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
servo = GPIO.PWM(11,50)
GPIO.setwarnings(False)

f=open("price.txt", "r")
l=  f.readlines()
if f.mode == 'r':
    price1 = l[1]
    price2 = l[2]
    price3 = l[3]
    price1 = int(price1)
    price2 = int(price2)
    price3 = int(price3)
pulses = 0

ser = serial.Serial('/dev/ttyUSB0', 9600)
while 1:
    
    if(ser.in_waiting >0):
        pulses = ser.readline()
        pulses = int(pulses.decode('ascii'))
        print(pulses)
                
        if pulses == price1:
            print("okay")
            order = price1
            ser.write(b'order')
            servo.start(0)
            servo.ChangeDutyCycle(2)
            time.sleep(.5)
            servo.ChangeDutyCycle(7)
            time.sleep(1.49)
            servo.ChangeDutyCycle(2)
            time.sleep(.5)
#            print("1")
            
        elif pulses == price2:
#            
            print("continue")

            ser.write(b'Y')
            servo.start(0)
            servo.ChangeDutyCycle(2)
            time.sleep(.5)
            servo.ChangeDutyCycle(7)
            time.sleep(1.49)
            servo.ChangeDutyCycle(2)
            time.sleep(.5)
    
        elif pulses == price3:
            print("okay")
            ser.write(b'Y')
            servo.start(0)
            servo.ChangeDutyCycle(2)
            time.sleep(.5)
            servo.ChangeDutyCycle(7)
            time.sleep(3.2)
            servo.ChangeDutyCycle(2)
            time.sleep(.5)
            
            
#        else:
#            print("not on list")
#                        print("3")
#                    if (order == 'N' or 'n'):
#                        pulses == price3
        
        
        
        
#        pulses = int(pulses)
#        if pulses == price1:
# #         print("You've inserted 50 pesos, press y to order and No to continue")
#            order = price1
#            ser.write(b'order')
#            servo.start(0)
#            servo.ChangeDutyCycle(2)
#            time.sleep(.5)
#            servo.ChangeDutyCycle(7)
#            time.sleep(1.49)
#            servo.ChangeDutyCycle(2)
#            time.sleep(.5)
#            print("1")
#            
#        elif pulses == price2:
#            
#              print("continue")
       
            
#            if (order == 'Y' or 'y'):
#                ser.write(b'Y')
#                servo.start(0)
#                servo.ChangeDutyCycle(2)
#                time.sleep(.5)
#                servo.ChangeDutyCycle(7)
#                time.sleep(1.49)
#                servo.ChangeDutyCycle(2)
#                time.sleep(.5)
#                print("1")
#            if (order == 'N' or 'n'):
#                pulses == price2
##        elif price1 > 50:
#            if pulses == price2:
##            print("Youve inserted 80 pesos, press y to order")
#                order = input()
#                if (order == 'Y' or 'y'):
#                    ser.write(b'Y')
#                    servo.start(0)
#                    servo.ChangeDutyCycle(2)
#                    time.sleep(.5)
#                    servo.ChangeDutyCycle(7)
#                    time.sleep(2.23)
#                    servo.ChangeDutyCycle(2)
#                    time.sleep(.5)
#                    print("2")
#                if (order == 'N' or 'n'):
#                    pulses == price2
#                if pulses == price3:
##            print("Youve inserted 100 pesos, press y to order")
#                    order = input()
#                    if (order == 'Y' or 'y'):
#                        ser.write(b'Y')
#                        servo.start(0)
#                        servo.ChangeDutyCycle(2)
#                        time.sleep(.5)
#                        servo.ChangeDutyCycle(7)
#                        time.sleep(3.2)
#                        servo.ChangeDutyCycle(2)
#                        time.sleep(.5)
#                        print("3")
#                    if (order == 'N' or 'n'):
#                        pulses == price3
