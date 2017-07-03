from __init__ import  *
import collections

class ChainDict(dict):
    '''
    Subclass of class dict which can be used to update a specific parameter value
    '''
    def set_key_chain(self, keyList, value):
        '''

        :param keyList:
        :param value:
        :return:
        '''
        t = self
        for k in keyList[:-1]:
            t = t.setdefault(k, {})
        t = t.setdefault(keyList[-1], value)

def searchParameter(parameterDictionary, parameterName):
    '''

    :param parameterDictionary:
    :param parameterName:
    :return:
    '''
    isPresent = False
    for k, v in parameterDictionary.iteritems():
        if isinstance(v, dict):
            isPresent = isPresent | searchParameter(v, parameterName)
            if isPresent == True:
                return isPresent
        if k == parameterName:
            isPresent = True
            return  isPresent
    return isPresent

def updateParameterValue(originalDict, updateDict):
    '''

    :param originalDict:
    :param updateDict:
    :return:
    '''
    for k, v in updateDict.iteritems():
        if isinstance(v, collections.Mapping):
            r = updateParameterValue(originalDict.get(k, {}), v)
            originalDict[k] = r
        else:
            originalDict[k] = updateDict[k]
    return originalDict

