from applications.factorial import get_factorial
from applications.user_interface import get_user_input, do_user_output

if __name__ == "__main__":
    initial_value = get_user_input()
    value_factorial = get_factorial(initial_value)
    do_user_output(value_factorial)
