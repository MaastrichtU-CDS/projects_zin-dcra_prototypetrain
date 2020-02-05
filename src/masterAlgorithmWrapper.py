from StationInterfaceFunctions import StationInterfaceFunctions
import json
from TaskDto import *

# ------ demo algorithm to demonstrate use of the Railway platform ------ 

# use the station interface to read all data
stationInterface = StationInterfaceFunctions()
inputStr = stationInterface.parseInputData()
completedClientTasks = stationInterface.parseCompletedTasks()

newTaskDtos = []
outputStr = ''
# --------------------------- PASTE YOUR ALGORITHM HERE -------------------------------
# to start the next iteration define the "newTaskDtos" variable
# to finish the final iteration define the "outputStr" varialble

# the input chosen is JSON, convert it now.
inputJson = json.loads(inputStr)
maxIterations = int(inputJson['iterations'])

# this is the one or multiple station run example
if completedClientTasks[0].iteration < maxIterations:
    newTaskDtos = []
    for task in completedClientTasks:
        newTask = TaskDto()
        newTask.stationId = task.stationId
        jsonOutput = json.loads(task.result)
        newTask.inputStr = json.dumps({'number_to_process': jsonOutput['calculation_result']})
        newTask.iteration = task.iteration + 1
        newTaskDtos.append(newTask)
else:
    #if last iteration
    try:
        output = 0
        for task in completedClientTasks:
            outputJson = json.loads(task.result)
            output = output + float(outputJson['calculation_result'])
    except:
        output = float('nan')

    outputStr = json.dumps({'total_sum': output})


# --------------------------- PASTE YOUR ALGORITHM HERE END ---------------------------
if newTaskDtos.__len__() > 0
    stationInterface.writeNewTasks(newTaskDtos)
stationInterface.writeOutputData(outputStr)