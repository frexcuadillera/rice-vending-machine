from time import sleep

import RPi.GPIO as GPIO

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 350)
servo.start(7.5)
sleep(1)
servo.ChangeDutyCycle(10)
sleep(1)
servo.ChangeDutyCycle(7.5)
sleep(1)
servo.ChangeDutyCycle(5)
sleep(1)
servo.stop()





# def setAngle(angle):
#     duty = angle / 18 + 3
#     #GPIO.output(11, True)
#     servo.ChangeDutyCycle(duty)
#     sleep(1)
#     #GPIO.output(11, False)
#     #servo.ChangeDutyCycle(duty)
    
#setAngle(90)