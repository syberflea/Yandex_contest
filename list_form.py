"""
Формат ввода
В первой строке — длина списочной формы числа X. На следующей строке — сама списочная форма с цифрами записанными через
пробел. В последней строке записано число K, 0 ≤ K ≤ 10000.

Формат вывода
Выведите списочную форму числа X+K.
"""
from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
    number = 0
    for power, num in enumerate(reversed(number_list)):
        number += num * pow(10, power)
    return str(number + k)

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))