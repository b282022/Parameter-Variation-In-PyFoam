from PyFoam.Execution import BasicRunner
from PyFoam.Applications import PlotRunner
from PyFoam.RunDictionary import ParsedParameterFile
from parameter_checker import ChainDict, modified_search_for_parameter, update_parameter_value
import latex_append
import os


def solve_for_a_particular_value(dict_file, key_to_change, current_value, solver):
    """
    Runs the simulation for current value of parameter
    Saves the plots of continuity and residuals and logs for current value of parameter
    :param dict_file: Parsed dictionary file (Type: ParsedParameterFile) which contains the parameter which is to be swept through iteration
    :param key_to_change: Parameter which is to be changed through out the simulation
    :param current_value: Current value of parameter
    :param solver: Name of solver to be used
    :return: Returns nothing
    """
    update_dict = ChainDict()
    update_dict.set_key_chain(key_to_change, current_value)

    update_parameter_value(original_dict=dict_file.__dict__['content'], update_dict=update_dict)
    dict_file.writeFile()

    block_mesh_runner = BasicRunner.BasicRunner(['blockMesh'])
    block_mesh_runner.start()

    plot_name = 'AtParameterValue' + str(current_value)

    PlotRunner.PlotRunner(['--hardcopy', '--prefix-hardcopy=' + plot_name, solver],
                          logname='PyFoam.' + plot_name)

    latex_file = open(key_to_change[-1] + '_Sweep.tex', 'a')
    latex_append.append_plot(latex_file=latex_file, plot_prefix=plot_name)
    latex_file.close()


def open_parsed_parameter_file(param_file_path):
    """
    The utility method that returns parsed dictionary object (of type ParsedParameterFile)
    which contains the parameter that has to be changed through out the simulation
    :param param_file_path: The path of dictionary file to be opened
    :return: The parsed dictionary object of type ParsedParameterFile
    """
    return ParsedParameterFile.ParsedParameterFile(param_file_path)


def is_valid_file(file_path):
    """
    Method to check if the given file path is correct or not
    :param file_path: The path of file
    :return: If the given file path is correct then returns True else returns False
    """
    if not os.path.exists(file_path):
        print "Entered path", file_path, "is wrong, Please try again!"
        return False
    return True


def is_parameter_variation_supported(file_path):
    """
    Method to check if file can be parsed using ParsedParameterFile utility of PyFOAM
    :param file_path: The path of dictionary/file which is to be parsed using ParsedParameterFile
    :return: If the file can be parsed then returns True else returns False
    """
    try:
        ParsedParameterFile.ParsedParameterFile(file_path)
    except AttributeError:
        print "Changing parameters of this file might not be supported! Sorry"
        return False
    return True


def is_valid_parameter(param_file, path_to_parameter):
    """
    Error check, if parameter exists or not
    :param param_file: The parameter file in which we can find the parameter we want to change
    :param path_to_parameter: The full path to parameter on which we want to iterate
    :return: bool: True if the path provided to parameter is correct else False
    """
    return modified_search_for_parameter(param_file.__dict__['content'], path_to_parameter, 0)
