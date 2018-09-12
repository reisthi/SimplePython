"""
    Assert is a build in python functionality that helps to identify error on your code.
    It makes it easier to debug your code by looking at the exception traceback and
    by easily identifying the root of an error.

    __________________________________________________________________________________
    Don't use asserts for:
        - Data Validation
        - Data Validation
"""


def apply_discount(price, discount):
    """ Shows how assert can be useful for wrong input values"""
    final_price = price * (1.0 - discount)
    # this ensures wrong discount values don't change the final price to a 0 or negative number
    assert 0 <= final_price <= price, 'final price <= 0'
    return final_price
