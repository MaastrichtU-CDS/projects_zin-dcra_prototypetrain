import json
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
        return output

    def parseCompletedTasks(self):
        fp = open(self._COMPLETED_TASK_PATH, 'r')
        raw_completed_tasks = json.load(fp)
        fp.close()
        taskDtos = []
        for task in raw_completed_tasks:
            taskDtos.append(TaskDto(task))
        return taskDtos

    def writeOutputData(self, outputStr):
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
