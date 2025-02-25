import sys

from applications.checkers import check_for_positive_integer


def get_user_input() -> int:
    """
    Function to get user input and check it before transfer to applications.
    Provides formatted console messages for better UX and notifying users about errors.
    :return: User input value converted to integer
    """
    for i in range(5):
        user_input = input('Введите целое положительное число.\nКо вводу допускаются только цифры: ')
        if not check_for_positive_integer(user_input):
            del user_input
            continue
        else:
            print(f'Все хорошо, начинаю вычисление факториала числа {user_input}')
            return int(user_input)
    sys.exit('Превышено количество попыток ввода. Пожалуйста, перезапустите программу.')


def calculation_complexity_warning_dialog():
    """
    Function provides user warning before calculations that might contain big numbers.
    It prevents dangerous loops on weak hardware and warn user before start.
    If the given number is big - we're asking user - to do or not to do. (Doo-do-doo)
    """
    print('Вычисление факториала числа от тысячи и больше может занять много ресурсов и времени.\n'
          'Вы уверены? (да / нет) ')
    user_answer = input().lower().strip()
    if user_answer == 'да':
        sys.set_int_max_str_digits(0)  # Provides ability to do display long values in console
    elif user_answer == 'нет':
        sys.exit('Выполнение программы прервано пользователем')
    else:
        print('Команда не распознана. Пожалуйста, повторите ввод\n')
        calculation_complexity_warning_dialog()


def do_user_output(initial: int, factorial: int):
    """
    This function is just a printer. It is small guy who working hard.
    :param initial: User input value
    :param factorial: Calculated factorial
    """
    print(f'Факториал числа {initial} вычислен и представлен ниже. Программа завершает работу\n{factorial}')
