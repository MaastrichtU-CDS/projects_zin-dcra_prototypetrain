import json, logging
def stationAlgorithm(inputStr):
    outputStr = ''
    logging.info('starting new calculation')
    # --------------------------- PASTE YOUR ALGORITHM HERE -------------------------------
    # define the "outputStr" variable
    # perform station algorithm
    inputJson = json.loads(inputStr)
    inputNumber = float(inputJson['number_to_process'])
    outputNum = inputNumber * 2
    outputStr = json.dumps({'calculation_result': outputNum})

    logging.info('done with calculation')

    return outputStr