class TaskDto:
	idNum = 0
	result = ""
	inputStr = ""
	stationId = 0
	calculationStatus = "REQUESTED"
	iteration = 0

	def __init__(self, taskDtoJson = None):
		if(taskDtoJson == None):
			return
		# self.idNum = taskDtoJson["id"]
		self.result = taskDtoJson["result"]
		self.inputStr = taskDtoJson["input"]
		self.calculationStatus = taskDtoJson["calculationStatus"]
		self.stationId = taskDtoJson["stationId"]
		self.iteration = taskDtoJson["iteration"]

	def export(self):
		taskDtoDict = {}
		taskDtoDict["result"] = self.result
		taskDtoDict["input"] = self.inputStr
		taskDtoDict["calculationStatus"] = self.calculationStatus
		taskDtoDict["stationId"] = self.stationId
		taskDtoDict["iteration"] = self.iteration
		return taskDtoDict