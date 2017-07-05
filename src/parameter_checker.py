import collections
import sys


class ChainDict(dict):
    """
    Subclass of class dict which can be used to update a specific parameter value
    """
    def set_key_chain(self, key_list, value):
        """
        Makes a nested dictionary which can be used as an argument in function update_parameter_value to change
        the parameter value
        :param key_list: The in-depth path to parameter
        :param value: New value of parameter
        :return:
        """
        t = self
        for k in key_list[:-1]:
            t = t.setdefault(k, {})
        t.setdefault(key_list[-1], value)


def search_parameter(parameter_dictionary, parameter_name):
    """
    Ignore this buggy method
    Just checks if there is a key with this name in nested dictionary
    Does not check it it follows exact path
    That is why made modified_search_for_parameter method
    :param parameter_dictionary:
    :param parameter_name:
    :return:
    """
    is_present = False
    for k, v in parameter_dictionary.iteritems():
        if isinstance(v, dict):
            is_present = is_present | search_parameter(v, parameter_name)
            if is_present:
                return is_present
        if k == parameter_name:
            is_present = True
            return  is_present
    return is_present


def modified_search_for_parameter(parameter_dictionary, path_to_parameter, counter):
    """
    Using recursion, Searches for the parameter in nested dictionary, in the exact sequence of the path provided
    :param parameter_dictionary: Parsed dictionary file
    :param path_to_parameter: Path to parameter
    :param counter: A variable to keep track of where we are currently in the path_to_parameter
    :return: bool: True if the path provided is correct else False
    """
    if counter > len(path_to_parameter):
        return False
    is_found = False
    for k, v in parameter_dictionary.iteritems():
        # print "Key", k
        if counter == len(path_to_parameter) - 1:
            if k == path_to_parameter[counter] and not isinstance(v, dict):
                return True
            elif k == path_to_parameter[counter] and isinstance(v, dict):
                return False
        if k == path_to_parameter[counter]:
            if isinstance(v, dict):
                return modified_search_for_parameter(v, path_to_parameter, counter + 1)
            return False
    return is_found


def update_parameter_value(original_dict, update_dict):
    """
    Using recursion we try to update the parameter in nested dictionary
    :param original_dict: The parsed dictionary file in which changes are to be made
    :param update_dict: Dictionary with updated value of parameter
    :return:
    """
    try:
        for k, v in update_dict.iteritems():
            if isinstance(v, collections.Mapping):
                r = update_parameter_value(original_dict.get(k, {}), v)
                original_dict[k] = r
            else:
                original_dict[k] = update_dict[k]
    except TypeError:
        print "Parameter Exists, But path supplied is wrong"
        sys.exit(1)
    return original_dict

