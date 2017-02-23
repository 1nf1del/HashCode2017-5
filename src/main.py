from model import Model
from firstAlgo import firstAlgo
import sys
import os

if len(sys.argv) == 1:
    print("Usage: python2 main.py [FILES]")

for filePath in sys.argv[1:]:
    inputFile = open(filePath)
    fileName,fileExtension = os.path.splitext(os.path.basename(filePath))
    outputFile = open(fileName + ".txt", "w")

    print("Importing file " + fileName + fileExtension)
    model = Model(inputFile)
    print("Model imported")
    inputFile.close()

    outputFile.write(firstAlgo(model))
    print("Output file " + fileName + ".txt generated")
    outputFile.close()

    print("Score: " + str(model.score()))
