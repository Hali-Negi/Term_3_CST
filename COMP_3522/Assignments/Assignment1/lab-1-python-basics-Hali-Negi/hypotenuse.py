import math


def calculate_hypotenuse(a, b):
    """
    Return the hypotenuse of a right-angled triangle.

    :param a: length of the first perpendicular side
    :param b: length of the second perpendicular side
    :return: length of the hypotenuse
    """
    return math.sqrt(a * a + b * b)
