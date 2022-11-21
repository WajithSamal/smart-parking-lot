import RPi.GPIO as GPIO

def indicate(place,color):
    GPIO.setmode(GPIO.BCM)

    gateGreen = 20
    gateRed = 21
    slotGreen = 23
    slotRed = 24

    GPIO.setup(gateGreen, GPIO.OUT)
    GPIO.setup(gateRed, GPIO.OUT)
    GPIO.setup(slotGreen, GPIO.OUT)
    GPIO.setup(slotRed, GPIO.OUT)

    if (place == 'g' and color == 'o'):
        GPIO.output(gateRed, True)
        GPIO.output(gateGreen, True)

    if (place == 'g' and color == 'r'):
        GPIO.output(gateRed, False)
        GPIO.output(gateGreen, True)

    if (place == 'g' and color == 'g'):
        GPIO.output(gateRed, True)
        GPIO.output(gateGreen, False)

    if (place == 's' and color == 'r'):
        GPIO.output(slotRed, False)
        GPIO.output(slotGreen, True)

    if (place == 's' and color == 'g'):
        GPIO.output(slotRed, True)
        GPIO.output(slotGreen, False)

    if (place == 's' and color == 'o'):
        GPIO.output(slotRed, True)
        GPIO.output(slotGreen, True)