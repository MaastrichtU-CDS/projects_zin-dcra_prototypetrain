from StationInterfaceFunctions import StationInterfaceFunctions
import json
import logging
from masterAlgorithm import *

# ------ demo algorithm to demonstrate use of the Railway platform ------ 
logging.basicConfig(filename='/opt/train.log',level=logging.DEBUG, format='%(asctime)s %(filename)s %(module)s %(funcName)s %(message)s')
logging.info('Starting a new master run')
try:
    # use the station interface to read all data
    stationInterface = StationInterfaceFunctions()
    inputStr = stationInterface.parseInputData()
    completedClientTasks = stationInterface.parseCompletedTasks()

    outputStr, newTaskDtos = masterAlgorithm(inputStr, completedClientTasks)

    # standard output
    stationInterface.writeNewTasks(newTaskDtos)
    stationInterface.writeOutputData(outputStr)
except Exception as e:
    logging.basicConfig(filename='/opt/error.log',level=logging.INFO, format='%(asctime)s %(message)s')
    logging.error(e, exc_info=True)
