def merge_dictionaries(d1, d2):
    """ Simple way to marge two dictionaries in python 3"""
    merged = {**d1, **d2}
    print(merged)
    return merged


dictionary1 = {'key1': 0}
dictionary2 = {'key2': 'another value'}

merge_dictionaries(dictionary1, dictionary2)
