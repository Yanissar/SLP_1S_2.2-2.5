from applications.checkers import check_for_positive_integer


def get_user_input():
    user_input = input('Введите целое положительное число.\nКо вводу допускаются только цифры: ')
    if check_for_positive_integer(user_input):
        print(f'Все хорошо, начинаю вычисление факториала числа {user_input}')
        return user_input
    else:
        get_user_input()
