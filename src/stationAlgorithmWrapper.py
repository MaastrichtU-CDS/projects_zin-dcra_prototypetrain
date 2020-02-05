from StationInterfaceFunctions import StationInterfaceFunctions
import json

# ------ demo algorithm to demonstrate use of the Railway platform ------ 

# use the station interface to read all data
stationInterface = StationInterfaceFunctions()
inputStr = stationInterface.parseInputData()

outputStr = ''
# --------------------------- PASTE YOUR ALGORITHM HERE -------------------------------
# define the "outputStr" varialble
# perform station algorithm
try:
    inputJson = json.loads(inputStr)
    inputNumber = float(inputJson['number_to_process'])
    outputNum = inputNumber * 2
except:
    outputNum = float('nan')

outputStr = json.dumps({'calculation_result': outputNum})
# --------------------------- PASTE YOUR ALGORITHM HERE END ---------------------------

# use the station interface to write all data
stationInterface.writeOutputData(outputStr)