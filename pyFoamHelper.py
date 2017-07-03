from __init__ import *

from PyFoam.Execution import BasicRunner
from PyFoam.Applications import PlotRunner
from PyFoam.RunDictionary import ParsedParameterFile


class PyFoamHelper:
    '''
    PyFoam Helper class with additional property of
    1) Automating parameter sweep
    2) Saving plots and logs
    '''

    def __init__(self):
        return

    def solveForAParticularValue(self, dictFile, keyToChange, currentValue, solver):
        '''
        Runs the simulation for current value of parameter
        Saves the plots of continuity and residuals and logs for current value of parameter
        :param dictFile: Parsed dictionary file (Type: ParsedParameterFile) which contains the parameter which is to be swept through iteration
        :param keyToChange: Parameter which is to be changed through out the simulation
        :param currentValue: Current value of parameter
        :param solver: Name of solver to be used
        :return: Returns nothing
        '''

        dictFile[keyToChange] = currentValue
        dictFile.writeFile()

        blockMeshRunner = BasicRunner.BasicRunner(['blockMesh'])
        blockMeshRunner.start()

        plotName = 'AtParameterValue' + str(currentValue)

        PlotRunner.PlotRunner(['--hardcopy', '--prefix-hardcopy=' + plotName, solver],
                              logname='PyFoam.' + plotName)

    def openParsedParameterFile(self, paramFilePath):
        '''
        The utility method that returns parsed dictionary object (of type ParsedParameterFile)
        which contains the parameter that has to be changed through out the simulation
        :param paramFilePath: The path of dictionary file to be opened
        :return: The parsed dictionary object of type ParsedParameterFile
        '''
        return ParsedParameterFile.ParsedParameterFile(paramFilePath)

    def isValidFile(self, filePath):
        '''
        Method to check if the given file path is correct or not
        :param filePath: The path of file
        :return: If the given file path is correct then returns True else returns False
        '''
        if not os.path.exists(filePath):
            print "Entered path", filePath, "is wrong, Please try again!"
            return False
        return True

    def isParameterVariationSupported(self, filePath):
        '''
        Method to check if file can be parsed using ParsedParameterFile utility of PyFOAM
        :param filePath: The path of dictionary/file which is to be parsed using ParsedParameterFile
        :return: If the file can be parsed then returns True else returns False
        '''
        try:
            t = ParsedParameterFile.ParsedParameterFile(filePath)
        except AttributeError:
            print "Changing parameters of this file might not be supported! Sorry"
            return False
        return True

    def isValidParameter(self, paramFile, parameterName):
        '''
        Error check, if parameter exists or not
        :param paramFile: The parameterFile in which we can find the parameter we want to change
        :param parameterName: The parameter on which we want to iterate
        :return: bool: True if the parameter exists in the file else False
        '''
        try:
            paramFile[parameterName]
        except KeyError:
            print "Invalid key"
            return False
        return True
