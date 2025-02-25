import math

from applications.user_interface import calculation_complexity_warning_dialog


def get_factorial(n):
    if n >= 1000:
        calculation_complexity_warning_dialog()
    return math.factorial(n)