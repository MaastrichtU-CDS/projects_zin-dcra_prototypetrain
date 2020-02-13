import json

def stationAlgorithm(inputStr):
    outputStr = ''
    # --------------------------- PASTE YOUR ALGORITHM HERE -------------------------------
    # define the "outputStr" variable
    # perform station algorithm
    try:
        inputJson = json.loads(inputStr)
        inputNumber = float(inputJson['number_to_process'])
        outputNum = inputNumber * 2
    except:
        outputNum = float('nan')

    outputStr = json.dumps({'calculation_result': outputNum})

    return outputStr