"""
Даны два числа в двоичной системе счисления, требуется  вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя.

Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе
"""
from typing import Tuple
from itertools import zip_longest


def get_sum(first_number: str, second_number: str) -> str:
    bin_sum = []
    carry = 0
    if first_number == '0':
        return second_number
    if second_number == '0':
        return first_number
    f_num = reversed(first_number)
    s_num = reversed(second_number)
    for f, s in zip_longest(f_num, s_num):
        if f and s:
            bin_res = int(f) + int(s) + carry
            if bin_res == 0:
                bin_sum.append('0')
                carry = 0
            elif bin_res == 1:
                bin_sum.append('1')
                carry = 0
            elif bin_res == 2:
                bin_sum.append('0')
                carry = 1
            elif bin_res == 3:
                bin_sum.append('1')
                carry = 1
        elif f and not s:
            bin_res = int(f) + carry
            if bin_res == 0:
                bin_sum.append('0')
                carry = 0
            elif bin_res == 1:
                bin_sum.append('1')
                carry = 0
            elif bin_res == 2:
                bin_sum.append('0')
                carry = 1
            elif bin_res == 3:
                bin_sum.append('1')
                carry = 1
        elif not f and s:
            bin_res = int(s) + carry
            if bin_res == 0:
                bin_sum.append('0')
                carry = 0
            elif bin_res == 1:
                bin_sum.append('1')
                carry = 0
            elif bin_res == 2:
                bin_sum.append('0')
                carry = 1
            elif bin_res == 3:
                bin_sum.append('1')
                carry = 1
    if carry:
        bin_sum.append('1')
    return "".join(reversed(bin_sum))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
