#import RPi.GPIO as GPIO
import time

class AlphaBot(object):  #classe dell'Alfabot
    
    def __init__(self, in1=13, in2=12, ena=6, in3=21, in4=20, enb=26):
        print("Inizializzazione")

    def backward(self, speed=80):  #avanti a velocità 60
        print("ROBOT INDIETRO")


    def stop(self):     #fermare i motori
        print("ROBOT STOP")


    def forward(self , speed = 60):   #indietro velocità 60
        print("ROBOT AVANTI")

        
        

    def left(self, speed = 25):     #girare a sinistra velocità settata in precedenza
        print("ROBOT SINISTRA")
        
    
    
    def right(self, speed = 25):    #destra con la velocità settata in precedenza
        print("ROBOT SINISTRA")
        
        
    def set_pwm_a(self, value):
        self.PA = value
        self.PWMA.ChangeDutyCycle(self.PA)

    def set_pwm_b(self, value):
        self.PB = value
        self.PWMB.ChangeDutyCycle(self.PB)    
        
    def set_motor(self, left, right):
        if (right >= 0) and (right <= 100):
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
            self.PWMA.ChangeDutyCycle(right)
        elif (right < 0) and (right >= -100):
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
            self.PWMA.ChangeDutyCycle(0 - right)
        if (left >= 0) and (left <= 100):
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
            self.PWMB.ChangeDutyCycle(left)
        elif (left < 0) and (left >= -100):
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.HIGH)
            self.PWMB.ChangeDutyCycle(0 - left)