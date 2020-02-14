import json, logging
from TaskDto import *

class StationInterfaceFunctions:
    _INPUT_PATH = '/opt/input.txt'
    _OUTPUT_PATH = '/opt/output.txt'
    _COMPLETED_TASK_PATH = '/opt/completed-client-tasks.json'
    _NEW_TASK_PATH = '/opt/new-client-tasks.json'

    def parseInputData(self):
        fp = open(self._INPUT_PATH, 'r')
        output = fp.read()
        fp.close()
        logging.debug('input data provided:')
        logging.debug(output)
        return output

    def parseCompletedTasks(self):
        fp = open(self._COMPLETED_TASK_PATH, 'r')
        raw_completed_tasks = json.load(fp)
        fp.close()
        logging.debug('completed tasks provided:')
        logging.debug(json.dumps(raw_completed_tasks))
        taskDtos = []
        for task in raw_completed_tasks:
            taskDtos.append(TaskDto(task))
        return taskDtos

    def writeOutputData(self, outputStr):
        logging.debug('output data provided:')
        logging.debug(outputStr)
        fp = open(self._OUTPUT_PATH, 'w+')
        fp.write(outputStr)
        fp.close()

    def writeNewTasks(self, newTaskDtos):
        newTasksList = []
        for task in newTaskDtos:
            newTasksList.append(task.export())
        fp = open(self._NEW_TASK_PATH, 'w+')
        json.dump(newTasksList, fp)
        fp.close()
        logging.debug('new tasks provided:')
        logging.debug(json.dumps(newTasksList))
