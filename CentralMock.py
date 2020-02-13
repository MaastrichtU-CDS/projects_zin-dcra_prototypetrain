import json, os, time, shutil, subprocess
from src.TaskDto import *
from distutils.dir_util import copy_tree

class CentralMock:
    _INPUT_PATH = './tmp/input.txt'
    _OUTPUT_PATH = './tmp/output.txt'
    _COMPLETED_TASK_PATH = './tmp/completed-client-tasks.json'
    _NEW_TASK_PATH = './tmp/new-client-tasks.json'
    _ERROR_PATH = './tmp/error.log'
    _LOG_PATH = './tmp/train.log'
    
    iteration = 0
    train_is_done = False
            
    def perfomMasterTask(self, inputStr, completedTaskDtos):
        self.startContainer()
        self.writeCompletedTaskJson(completedTaskDtos)
        self.writeInput(inputStr)
        self.copyFilesToDocker()
        os.system('docker exec test_train sh /runMaster.sh')
        self.copyFilesFromDocker()
        self.stopContainer()
        return self.readOutput(), self.readNewTasks()

    def perfomStationTask(self, inputStr):
        self.startContainer()
        self.writeInput(inputStr)
        self.copyFilesToDocker()
        os.system('docker exec test_train sh /runStation.sh')
        self.copyFilesFromDocker()
        self.stopContainer()
        return self.readOutput()
        
    def writeCompletedTaskJson(self, taskDtos):
        tasksList = []
        for task in taskDtos:
            tasksList.append(self.exportTaskDtoWithId(task))
        fp = open(self._COMPLETED_TASK_PATH, 'w+')
        json.dump(tasksList, fp)
        fp.close()
        
    def writeInput(self, inputStr):
        fp = open(self._INPUT_PATH, 'w+')
        fp.write(inputStr)
        fp.close()
        
    def readOutput(self):
        fp = open(self._OUTPUT_PATH, 'r')
        output = fp.read()
        fp.close()
        return output

    def readNewTasks(self):
        fp = open(self._NEW_TASK_PATH, 'r')
        output = fp.read()
        fp.close()
        return json.loads(output)
    
    def copyFilesToDocker(self):
        subprocess.call('docker cp ./tmp/. test_train:/opt', shell=True)
        
    def copyFilesFromDocker(self):
        subprocess.call('docker cp test_train:/opt/. ./tmp', shell=True)
        
    def startContainer(self):
        #start train (like Station would)
        subprocess.call('docker run -d -it --name=test_train test_train', shell=True)
        
    def stopContainer(self):
        #stop train (like Station would)
        subprocess.call('docker stop test_train', shell=True)
        subprocess.call('docker rm test_train', shell=True)
        
    def doesContainerRespond(self):
        result = subprocess.run('docker ps', shell=True, stdout=subprocess.PIPE)
        docker_ps = result.stdout.decode("utf-8")
        if docker_ps.find('test_train') != -1:
            return True
        else:
            return False

    def clearTmpFolder(self):
        if os.path.lexists('./tmp/'):
            shutil.rmtree('./tmp/')
            os.mkdir('./tmp/')

    def clearTrainFolder(self):
        if os.path.lexists('./train/'):
            shutil.rmtree('./train/')
            os.mkdir('./train/')
        
    def archiveRun(self, master, iteration, stationId):
        if master:
            iteration_dir = os.path.join('./train','iteration_' + str(iteration), 'master', 'station_id_' + str(stationId))
        else:
            iteration_dir = os.path.join('./train','iteration_' + str(iteration), 'station', 'station_id_' + str(stationId))
        if not os.path.lexists(iteration_dir):
            os.makedirs(iteration_dir)
        copy_tree('./tmp', iteration_dir)
        self.clearTmpFolder()
        

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