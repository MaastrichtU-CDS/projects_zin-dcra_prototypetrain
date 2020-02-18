import json, logging
from TaskDto import TaskDto

# To start the next iteration define the "newTaskDtos" variable.
# To finish the final iteration do not define the "newTaskDtos" variable.
def masterAlgorithm(inputStr, completedClientTasks):
    newTaskDtos = []
    outputStr = ''
    logging.info('starting new master task')

    # the input chosen is JSON, convert it now.
    inputJson = json.loads(inputStr)
    maxIterations = int(inputJson['iterations'])
    
    # This is a multiple station run example.
    if completedClientTasks[0].iteration < maxIterations:
        logging.info('master not done yet, setting up the next iteration')
        newTaskDtos = []
        for task in completedClientTasks:
            newTask = TaskDto()
            newTask.stationId = task.stationId
            jsonOutput = json.loads(task.result)
            newTask.inputStr = json.dumps({'number_to_process': jsonOutput['calculation_result']})
            newTask.iteration = task.iteration + 1
            newTaskDtos.append(newTask)

            #If there are new tasks, a new master task will be created in central.
            #The output of the current task will be the input for the next master task.
            #As an example the iterations variable is passed on without alterations.
            outputStr = inputStr
    else:
        logging.info('master is done, calculating final result')

        output = 0
        for task in completedClientTasks:
            outputJson = json.loads(task.result)
            output = output + float(outputJson['calculation_result'])
        outputStr = json.dumps({'total_sum': output})
        #No newTasks are defined here, so the station algorithm will assume this was the last master iteration.
        
    return outputStr, newTaskDtos