import sys

from applications.checkers import check_for_positive_integer


def get_user_input():
    user_input = input('Введите целое положительное число.\nКо вводу допускаются только цифры: ')
    if check_for_positive_integer(user_input):
        print(f'Все хорошо, начинаю вычисление факториала числа {user_input}')
        return int(user_input)
    else:
        get_user_input()


def calculation_complexity_warning_dialog():
    print('Вычисление факториала числа от тысячи и больше может занять много ресурсов и времени.\n'
          'Вы уверены? (да / нет) ')
    user_answer = input().lower().strip()
    if user_answer == 'да':
        sys.set_int_max_str_digits(0)
    elif user_answer == 'нет':
        sys.exit('Выполнение программы прервано пользователем')
    else:
        print('Команда не распознана. Пожалуйста, повторите ввод\n')
        calculation_complexity_warning_dialog()


def do_user_output(calculation_value):
    print(calculation_value)
