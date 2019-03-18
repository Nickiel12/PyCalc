import pathlib
import datetime

now = datetime.datetime.now()

def SaveToFile(fileContents, CalcType, outputFile = 'Time', outputFolder = "Output"):
    outputFolder = pathlib.PurePath(outputFolder)

    if outputFile == 'Time':
        nowSt = str(now)[:str(now).find(".")].replace("-", "_").replace(":", "-")
        filePath = outputFolder / 'Output_{}_{}.txt'.format(CalcType, nowSt)
    else:
        filePath = outputFolder / 'Output_{}.txt'.format(outputFile)

    if isinstance(fileContents, str):
        with open(filePath, 'w') as file:
            file.write(fileContents)

    elif isinstance(fileContents, list):
        with open(filePath, 'a') as file:
            for i in fileContents:
                file.write(i+"\n")
    