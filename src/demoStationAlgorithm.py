from StationInterfaceFunctions import StationInterfaceFunctions
import json

# ------ demo algorithm to demonstrate use of the Railway platform ------ 

# use the station interface to read all data
stationInterface = StationInterfaceFunctions()
inputStr = stationInterface.parseInputData()

# perform station algorithm
try:
    inputNumber = float(inputStr)
    outputStr = str(inputNumber * 2)
except:
    outputStr = float('nan')

# use the station interface to write all data
stationInterface.writeOutputData(outputStr)