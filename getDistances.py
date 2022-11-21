import RPi.GPIO as GPIO
import time


def readSensors():
    dist = [getRead()[0] < 20, getRead()[1] < 20, getRead()[2] < 20]
    return dist


def getRead():
    GPIO.setmode(GPIO.BCM)
    trigList = [19, 6, 27]
    echoList = [26, 13, 22]
    dis = []
    for i in range(3):
        dis.append(distance(trigList[i], echoList[i]))
    return dis


def distance(trig, echo):
    d = 0
    while (d == 0):
        GPIO_TRIGGER = trig
        GPIO_ECHO = echo

        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        startTime = time.time()
        timeInit = startTime

        while GPIO.input(GPIO_ECHO) == 0:
            startTime = time.time()
            if (startTime - timeInit > 0.5):
                break

        stopTime = time.time()
        timeInit = stopTime
        while GPIO.input(GPIO_ECHO) == 1:
            stopTime = time.time()
            if (stopTime - timeInit > 0.5):
                break

        dT = stopTime - startTime
        d = (dT * 34300) / 2
        if (d > 3000):
            d = 0
    return d
