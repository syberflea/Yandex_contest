"""
Задача
Напишите программу, которая будет принимать данные для определённого раунда:
значение k,
значения для кнопок,
и вычислит количество баллов, которое будут заработано в этом раунде.

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках заданы значения для кнопок –— по 4 символа в каждой строке. Каждый символ —– либо точка,
либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— количество баллов, которое игроки наберут в раунде.
"""
import sys
from typing import List, Tuple
from collections import Counter

ROWS = 4
def read_input() -> Tuple[int, List[str]]:
    number_list = []
    n = int(input())
    for _ in range(ROWS):
        number_list.append(input().strip())
    return n, number_list


def read_input_2() -> list[str]:
    lines = sys.stdin.readlines()
    number_list = []
    for line in lines:
        number_list.append(line.strip())
    return number_list


def count_points(k: int, lines: List[str]) -> int:
    points_dict = {}
    points = 0
    cnt = Counter()
    for line in lines:
        cnt += Counter(line)
    points_dict.update(cnt)
    for key, val in points_dict.items():
        if key == '.':
            continue
        if val <= k * 2:
            points += 1
    return points


k, keyboard = read_input()
print(keyboard)
print(count_points(k, keyboard))
