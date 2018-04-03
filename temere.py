"""
    Temere stands for Random in Latin.
"""


def laplace_law(w, n):
    """Laplace’s law  attempts to calculate the probability
    of an event happening based on its previous ongoings.
    The rule is: calculate the number of times it has happened
    in the past (w) plus one, then divide by the number of opportunities (n) plus 2.
    """
    result = ((w + 1) / (n + 2)) * 100
    return print(" {} % chance".format(result))
