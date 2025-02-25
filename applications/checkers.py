def check_for_positive_integer(number: str) -> bool:
    """
    Function to check if user input is actually a number and it is positive.
    :param number: User input from get_user_input()
    :return: Boolean flag for conditional operator in get_user_input()
    """
    checking_mode = True
    if len(number) == 0:
        checking_mode = False
        print(f'\nОшибка. Кажется, вы ввели пустое значение.\n'
              f'Пожалуйста, введите целое положительное число.\n')
    elif not number.isdigit():
        checking_mode = False
        print(f'\nОшибка. На входе получено недопустимое значение.\n'
              f'Пожалуйста, введите целое положительное число, используя цифры.\n')
    elif int(number) < 0:
        checking_mode = False
        print(f'\nОшибка. Кажется, вы ввели отрицательное число.\n'
              f'Пожалуйста, введите целое положительное число.\n')
    return checking_mode
