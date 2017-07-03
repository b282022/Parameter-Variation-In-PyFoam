#!/usr/bin/python

# System Inbuilt imports
from __init__ import *
import sys

# My imports
import constants
from pyFoamHelper import PyFoamHelper
import time
import latex_append

# import pdb; pdb.set_trace()

PyFoamHelperObject = PyFoamHelper()
# Path of the dictionary file, in which the parameter has to be swept
pathOfDict = sys.argv[1]

# If the path entered is wrong
if not PyFoamHelperObject.isValidFile(pathOfDict):
    sys.exit(1)

# If the file which contains the parameter is not supported by parser
if not PyFoamHelperObject.isParameterVariationSupported(pathOfDict):
    sys.exit(1)


# Parsed parameter file object
parameterFile = PyFoamHelperObject.openParsedParameterFile(pathOfDict)

# The parameter which has to be swept
keyToBeChanged = sys.argv[2].split('/')

# If exists, store initial value of parameter somewhere so after all itertations you can put it back
if not PyFoamHelperObject.isValidParameter(parameterFile, keyToBeChanged[-1]):
    print "Parameter", keyToBeChanged[-1]," Not found, Please enter correct parameter!"
    sys.exit(1)

# initialValue = parameterFile[keyToBeChanged]


# The range of parameter in start:delta:final format
parameterSweep = sys.argv[3].split(":")
if len(parameterSweep) < 3:
    print "Please give input in proper format which can be parsed in floats!"
    sys.exit(1)


try:
    startValueOfKey = float(parameterSweep[0])
    incrementalValue = float(parameterSweep[1])
    finalValueOfKey = float(parameterSweep[2])
except ValueError:
    print "Please give input in proper format which can be parsed in floats!"
    sys.exit(1)

if finalValueOfKey  < startValueOfKey:
    print "Please provide range in proper formats!"
    sys.exit(1)

solver = sys.argv[4]
if not constants.existsSolver(solver):
    print "Not a valid OpenFOAM solver, Please try again!"
    sys.exit(1)


# Write header of latex file
latexFileName = keyToBeChanged[-1] + '_Sweep.tex'
latexFile = open(latexFileName, 'w')
latex_append.writeHeader(latexFile, latexFileName)
latexFile.close()

currentParameterValue = startValueOfKey

# Run iterations for different values of parameter
while currentParameterValue <= finalValueOfKey:
    PyFoamHelperObject.solveForAParticularValue(dictFile=parameterFile, keyToChange=keyToBeChanged, currentValue=currentParameterValue,
                             solver=solver)

    currentParameterValue += incrementalValue

time.sleep(5)

# Rename plots
print "Renaming Files"
currentParameterValue = startValueOfKey
while currentParameterValue <= finalValueOfKey:
    plotName = 'AtParameterValue' + str(currentParameterValue)

    imageName = plotName
    split = plotName.split(".")

    if(len(split)) == 2:
        imageName = split[0] + "_" + split[1]

    os.rename(plotName + '.linear.png', imageName + 'linear.png')
    os.rename(plotName + '.cont.png', imageName + 'cont.png')
    currentParameterValue += incrementalValue

# Write footer of latex file
latexFile = open(latexFileName, 'a')
latex_append.writeFooter(latexFile)
latexFile.close()

# Save the original file back
# parameterFile[keyToBeChanged] = initialValue
#   parameterFile.writeFile()
