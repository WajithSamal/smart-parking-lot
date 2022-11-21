from gpiozero import Servo

servo=Servo(5)

def gateOpen():
    servo.min()

def gateClose():
    servo.max()