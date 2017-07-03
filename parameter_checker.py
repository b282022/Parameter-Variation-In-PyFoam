import collections


class ChainDict(dict):
    """
    Subclass of class dict which can be used to update a specific parameter value
    """
    def set_key_chain(self, key_list, value):
        """
        :param key_list:
        :param value:
        :return:
        """
        t = self
        for k in key_list[:-1]:
            t = t.setdefault(k, {})
        t.setdefault(key_list[-1], value)


def search_parameter(parameter_dictionary, parameter_name):
    """
    :param parameter_dictionary:
    :param parameter_name:
    :return:
    """
    is_present = False
    for k, v in parameter_dictionary.iteritems():
        if isinstance(v, dict):
            is_present = is_present | search_parameter(v, parameter_name)
            if is_present == True:
                return is_present
        if k == parameter_name:
            is_present = True
            return  is_present
    return is_present


def update_parameter_value(original_dict, update_dict):
    """
    :param original_dict:
    :param update_dict:
    :return:
    """
    for k, v in update_dict.iteritems():
        if isinstance(v, collections.Mapping):
            r = update_parameter_value(original_dict.get(k, {}), v)
            original_dict[k] = r
        else:
            original_dict[k] = update_dict[k]
    return original_dict

