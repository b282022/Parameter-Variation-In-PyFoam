#!/usr/bin/python

# System Inbuilt imports
import time

# My imports
import constants
import pyFoamHelper
import sys
import latex_append
import utilities

if len(sys.argv) == 2:
    if sys.argv[1] == '--help':
        utilities.print_help_message()
        sys.exit(0)
    else:
        print "Too few arguments"
        utilities.print_help_message()
        sys.exit(2)

elif len(sys.argv) < 5:
    print "Too few arguments"
    utilities.print_help_message()
    sys.exit(2)

# Path of the dictionary file, in which the parameter has to be swept
pathOfDict = sys.argv[1]

# If the path entered is wrong
if not pyFoamHelper.is_valid_file(pathOfDict):
    sys.exit(1)

# If the file which contains the parameter is not supported by parser
if not pyFoamHelper.is_parameter_variation_supported(pathOfDict):
    sys.exit(1)

# Parsed parameter file object
parameterFile = pyFoamHelper.open_parsed_parameter_file(pathOfDict)

# The parameter which has to be swept
keyToBeChanged = sys.argv[2].split('/')

# If exists, store initial value of parameter somewhere so after all itertations you can put it back
if not pyFoamHelper.is_valid_parameter(parameterFile, keyToBeChanged):
    print "Parameter", sys.argv[2], " Not found, Please enter correct parameter!"
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

if finalValueOfKey < startValueOfKey:
    print "Please provide range in proper formats!"
    sys.exit(1)

solver = sys.argv[4]
if not constants.exists_solver(solver):
    print "Not a valid OpenFOAM solver, Please try again!"
    sys.exit(1)

# Write header of latex file
latexFileName = keyToBeChanged[-1] + '_Sweep.tex'
latexFile = open(latexFileName, 'w')
latex_append.write_header(latexFile, latexFileName)
latexFile.close()

currentParameterValue = startValueOfKey

# Run iterations for different values of parameter
while currentParameterValue <= finalValueOfKey:
    pyFoamHelper.solve_for_a_particular_value(dict_file=parameterFile, key_to_change=keyToBeChanged,
                                              current_value=currentParameterValue,
                                              solver=solver)

    currentParameterValue += incrementalValue

time.sleep(5)

# Rename plots after simulation for each value is done
utilities.rename_files(startValueOfKey, incrementalValue, finalValueOfKey)

# Write footer of latex file
latexFile = open(latexFileName, 'a')
latex_append.write_footer(latexFile)
latexFile.close()
