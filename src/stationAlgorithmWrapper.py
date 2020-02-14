from StationInterfaceFunctions import StationInterfaceFunctions
import json
import logging
from stationAlgorithm import *

# ------ demo algorithm to demonstrate use of the Railway platform ------ 
logging.basicConfig(filename='/opt/train.log',level=logging.DEBUG, format='%(asctime)s %(filename)s %(module)s %(funcName)s %(message)s')
logging.info('Starting a new station run')
try:
    # use the station interface to read all data
    stationInterface = StationInterfaceFunctions()
    inputStr = stationInterface.parseInputData()

    outputStr = stationAlgorithm(inputStr)

    # use the station interface to write all data
    stationInterface.writeOutputData(outputStr)
except Exception as e:
    logging.error(e, exc_info=True)
    logging.basicConfig(filename='/opt/error.log',level=logging.INFO, format='%(asctime)s %(message)s')
    logging.error(e, exc_info=True)    