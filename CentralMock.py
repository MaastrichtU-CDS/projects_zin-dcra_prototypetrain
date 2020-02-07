import json
import os
from src.TaskDto import *
import subprocess

class CentralMock:
    _INPUT_PATH = './tmp/input.txt'
    _OUTPUT_PATH = './tmp/output.txt'
    _COMPLETED_TASK_PATH = './tmp/completed-client-tasks.json'
    _NEW_TASK_PATH = './tmp/new-client-tasks.json'
    
    iteration = 0
    train_is_done = False
    masterOutput = ''
    
    def __init__(self):
        self.stationIterations = dict()
        self.masterItetations = dict()
    
    def setTasksForStationIteration(self, tasks, iteration):
        self.stationIterations[iteration] = completedTasks
        
    def setMasterTaskForIteration(self, task, iteration):
#         task = TaskDto()
#         task.idNum = completedTasks.__len__() + 1
#         task.inputStr = masterInput
        self.masterItetations[0] = task
    
    def performStationTasks(self):
        tasks = self.iteration[0]
        for taskDto in tasks:
            if taskDto.calculationStatus == 'REQUESTED':
                #do something
                taskDto.calculationStatus == "COMPLETED"
                return
            else:
                completed = completed + 1
        if self.stationTasks.__len__ == completed:
            #create new master task
            print('create new master task')
            print(self.stationTasks)
            
    def perfomMasterTask(self):
        self.startContainer()
        self.writeTaskJson()
        self.writeMasterInput()
        self.copyMasterFilesToDocker()
        os.system('docker exec test_train sh /runMaster.sh')
        self.copyMasterOutputFromDocker()
        self.stopContainer()
        return self.readOutput()
        
    def writeTaskJson(self):
        tasksList = []
        taskDtos = self.stationIterations[self.iteration]
        for task in taskDtos:
            tasksList.append(self.exportTaskDtoWithId(task))
        fp = open(self._COMPLETED_TASK_PATH, 'w+')
        json.dump(tasksList, fp)
        fp.close()
        
    def writeMasterInput(self):
        fp = open(self._INPUT_PATH, 'w+')
        fp.write(self.masterItetations[self.iteration].inputStr)
        fp.close()
        
    def readOutput(self):
        fp = open(self._OUTPUT_PATH, 'r')
        output = fp.read()
        fp.close()
        return output
    
    def copyMasterFilesToDocker(self):
        subprocess.call('docker cp ' + self._COMPLETED_TASK_PATH + ' test_train:/opt/completed-client-tasks.json')
        subprocess.call('docker cp ' + self._INPUT_PATH + ' test_train:/opt/input.txt')
        
    def copyMasterOutputFromDocker(self):
        subprocess.call('docker cp test_train:/opt/output.txt ' + self._OUTPUT_PATH)
        
    def copyOutputFromDocker(self):
        print('')
        
    def startContainer(self):
        #start train (like Station would)
        subprocess.call('docker run -d -it --name=test_train test_train')
        
    def stopContainer(self):
        #stop train (like Station would)
        subprocess.call('docker stop test_train')
        subprocess.call('docker rm test_train')
        
    def doesContainerRespond(self):
        result = subprocess.run('docker ps', shell=True, stdout=subprocess.PIPE)
        docker_ps = result.stdout.decode("utf-8")
        if docker_ps.find('test_train') != -1:
            return True
        else:
            return False
        
    #this functions is needed because the export cannot export id for the Java app but we need it here
    def exportTaskDtoWithId(self, task):
        taskDtoDict = {}
        taskDtoDict["id"] = task.idNum
        taskDtoDict["result"] = task.result
        taskDtoDict["input"] = task.inputStr
        taskDtoDict["calculationStatus"] = task.calculationStatus
        taskDtoDict["stationId"] = task.stationId
        taskDtoDict["iteration"] = task.iteration
        return taskDtoDict