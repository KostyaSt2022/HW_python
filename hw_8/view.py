from fractions import Fraction #поддержка рациональных чисел
import math

def get_value():
    value = input('Введите число: ')
    try:
        value = Fraction(value)
        return value
    except ValueError:
        value = complex(value)
        return value


def get_operator():
    oper = input('Введите оператор: ')
    return oper


def get_result(res):
    print(f'Результат: {res}')