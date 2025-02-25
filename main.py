from applications.factorial import get_factorial
from applications.user_interface import get_user_input, do_user_output


def main():
    """
    Base procedure for running the application.
    Just running scripts in correct order.
    For more details, please see the documentation at: README.md
    """
    initial_value = get_user_input()
    factorial_value = get_factorial(initial_value)
    do_user_output(initial_value, factorial_value)


if __name__ == "__main__":
    main()
