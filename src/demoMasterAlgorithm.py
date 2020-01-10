from StationInterfaceFunctions import StationInterfaceFunctions
import json
from TaskDto import *

# ------ demo algorithm to demonstrate use of the Railway platform ------ 

# use the station interface to read all data
stationInterface = StationInterfaceFunctions()
inputStr = stationInterface.parseInputData()
completedClientTasks = stationInterface.parseCompletedTasks()

# perform master algorithm, this demo makes new tasks for the stations selected and combines their result into a final result
# if(completedClientTasks.__len__ > 0 & not completedClientTasks[0].result):
if completedClientTasks.__len__() > 0:
    if not completedClientTasks[0].result:
        # this is the first run
        newTaskDtos = []
        for task in completedClientTasks:
            newTask = TaskDto()
            newTask.stationId = task.stationId
            newTask.inputStr = task.inputStr
            newTaskDtos.append(newTask)

        stationInterface.writeNewTasks(newTaskDtos)
    else:
        #this is the second run
        try:
            sumOfNumbers = 0
            for task in completedClientTasks:
                sumOfNumbers = sumOfNumbers + float(task.result)
            outputStr = str(sumOfNumbers)
        except:
            outputStr = str(float('nan'))
        stationInterface.writeOutputData(outputStr)
else:
    print("no client information found, cannot create station tasks")
