import math

from applications.user_interface import calculation_complexity_warning_dialog


def get_factorial(n: int) -> int:
    """
    Calculating !n, using math.factorial() and return to printer
    :param n: Value to calculate factorial for
    :return: Factorial of n
    """
    if n >= 1000:
        calculation_complexity_warning_dialog()
    return math.factorial(n)
