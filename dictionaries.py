dict_one = {'one': 1, 'two': 2}
dict_two = {'three': 3, 'four': 4}


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
    return wip.updates(dict_two)


def merge_merges(wip, wip_two):
    """ Simple way to marge two dictionaries in python 3. """
    # ** is the magic, details on the brackets
    return {**wip, **wip_two}


def dict_copy(wip):
    """ Returns a shallow copy of a dictionary. """
    copy_of_dict = wip.copy()
    return copy_of_dict


def dict_clear(wip):
    """ Deletes all key-values of a dictionary. """
    return wip.clear()
