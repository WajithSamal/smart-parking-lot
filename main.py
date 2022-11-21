import time

import camera
import databaseCom
import gateControl
import getDistances
import indicators

while True:
    indicators.indicate('g', 'o')
    distances = getDistances.readSensors()

    if (distances[0] == True):
        indicators.indicate('g', 'r')
        camera.readQR()
        indicators.indicate('g', 'g')
        gateControl.gateOpen()
        databaseCom.arrived()
        while (distances[1] == False):
            distances = getDistances.readSensors()
        time.sleep(2)
        indicators.indicate('g', 'o')
        gateControl.gateClose()
        while (distances[3] == False):
            distances = getDistances.readSensors()
        indicators.indicate('g', 'r')


    if (databaseCom.status == 0):
        indicators.indicate('s', 'o')

    if (databaseCom.status == 2):
        indicators.indicate('s', 'r')

    if(databaseCom.status == 3 and distances[3] == False):
        databaseCom.departed()
        gateControl.gateOpen()
        while (distances[0] == False):
            distances = getDistances.readSensors()
        time.sleep(2)
        gateControl.gateClose()
        indicators.indicate('s', 'o')