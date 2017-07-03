import os


def rename_files(start_value, incremental_value, final_value):

    """
    Rename plots after simulation for each value is done
    Method renames files to a format such that, it can be added in such a way that LaTeX file compiles
    :param start_value: The initial value of range with which the parameter starts changing its value
    :param incremental_value: The value with which the parameter increases its value
    :param final_value: The final value of parameter
    :return: void
    """

    while start_value <= final_value:
        plotName = 'AtParameterValue' + str(start_value)

        imageName = plotName
        split = plotName.split(".")

        if (len(split)) == 2:
            imageName = split[0] + "_" + split[1]

        os.rename(plotName + '.linear.png', imageName + 'linear.png')
        os.rename(plotName + '.cont.png', imageName + 'cont.png')
        start_value += incremental_value


def print_help_message():

    """
    Help message about how to use this script and how to give command line arguments
    :return: Nothing
    """

    print "Four arguments required <path_of_dictionary_file> <parameter_name> <range_of_parameter> <name_of_solver>"
    print "1) Whole path of the file in which the parameter to change is stored"
    print "\t For example, if you want to open controlDict file in system directory type ./system/controlDict"
    print "2) The full in-depth path to parameter which is to be changed over a given range of value"
    print "\t For example, if you want to change tolerance of p in the file fvSolution type solvers/p/tolerance"
    print "3) The range of values for which the parameter is to be changed"
    print """\t For example, if you want to change tolerance of p from 0.000001 to 0.000005 at intervals of 0.000001 
    \t type 0.00001:0.000001:0.0.000005"""
    print "4) The name of solver which you want to use"
    print "\t For example, if you want to use icoFoam then type icoFoam"
