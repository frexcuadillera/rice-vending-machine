
import time
# # 
import RPi.GPIO as GPIO
# #
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)
# # 
servo.start(2)
time.sleep(.27)
servo.ChangeDutyCycle(7)
time.sleep(1.49)
servo.ChangeDutyCycle(2)
time.sleep(.27)
servo.stop()
###
GPIO.cleanup()


# def setAngle(angle):
#     duty = angle / 18 + 3
#     #GPIO.output(11, True)
#     servo.ChangeDutyCycle(duty)
#     sleep(1)
#     #GPIO.output(11, False)
#     #servo.ChangeDutyCycle(duty)
    
#setAngle(90)

import time
#!/usr/bin/env python
'''
#sudo pigpiod
import pigpio
 
pi = pigpio.pi('soft', 8888) # Connect to local Pi.
 
pi.set_servo_pulsewidth(17, 1000)
time.sleep(0.5)
pi.set_servo_pulsewidth(17, 1500)
'''