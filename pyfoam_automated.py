#!/usr/bin/python

# System Inbuilt imports
from __init__ import *
import sys

# My imports
import constants
from pyFoamHelper import PyFoamHelper

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
keyToBeChanged = sys.argv[2]

# If exists, store initial value of parameter somewhere so after all itertations you can put it back
if not PyFoamHelperObject.isValidParameter(parameterFile, keyToBeChanged):
    sys.exit(1)
initialValue = parameterFile[keyToBeChanged]


# The range of parameter in start:delta:final format
parameterSweep = sys.argv[3].split(":")
try:
    startValueOfKey = float(parameterSweep[0])
    incrementalValue = float(parameterSweep[1])
    finalValueOfKey = float(parameterSweep[2])
except ValueError:
    print "Please give input in proper format which can be parsed in floats!"
    sys.exit(1)

solver = sys.argv[4]
if not constants.existsSolver(solver):
    print "Not a valid OpenFOAM solver, Please try again!"
    sys.exit(1)

currentParameterValue = startValueOfKey

# Run iterations for different values of parameter
while currentParameterValue <= finalValueOfKey:
    PyFoamHelperObject.solveForAParticularValue(dictFile=parameterFile, keyToChange=keyToBeChanged, currentValue=currentParameterValue,
                             solver=solver)

    currentParameterValue += incrementalValue

# Save the original file back
parameterFile[keyToBeChanged] = initialValue
parameterFile.writeFile()
