wip = {'one': 1, 'two': 2}
wip_two = {'one': 1, 'two': 2}


def display_dict(wip):
    """ Returns all the items of a dictionary. """
    # name_of_the_dict.items()
    return wip.items()


def dict_values(wip):
    """ Get the values of a dictionary. """
    # name_of_the_dict.values()
    return wip.values()


def dict_update(wip):
    """ Adds a dictionary to the current dictionary. """
    # name_of_the_dict_one.updates(name_of_dict_2)
    return wip.updates(wip_two)


def merge_merges(dict_one, dict_two):
    """ Simple way to marge two dictionaries in python 3"""
    # ** is the magic, details on the brackets
    return {**dict_one, **dict_two}

