import json, logging
from TaskDto import TaskDto

# To start the next iteration define the "newTaskDtos" variable.
# To finish the final iteration do not define the "newTaskDtos" variable.
def masterAlgorithm(inputStr, completedClientTasks):
    newTaskDtos = []
    outputStr = ''
    logging.info('starting new master task')

    outputStr = completedClientTasks[0].result
        
    return outputStr, newTaskDtos