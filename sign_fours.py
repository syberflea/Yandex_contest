"""
Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4^n, где n – целое неотрицательное число.
"""
from math import log, floor
def is_power_of_four(number: int) -> bool:
    return bool(floor(log(number, 4)) == log(number, 4))

print(is_power_of_four(int(input())))