from StationInterfaceFunctions import StationInterfaceFunctions
import json
from stationAlgorithm import *

# ------ demo algorithm to demonstrate use of the Railway platform ------ 

try:
    # use the station interface to read all data
    stationInterface = StationInterfaceFunctions()
    inputStr = stationInterface.parseInputData()

    outputStr = stationAlgorithm(inputStr)

    # use the station interface to write all data
    stationInterface.writeOutputData(outputStr)