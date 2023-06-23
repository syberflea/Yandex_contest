"""
ID: 88446509
"""
from typing import List, Tuple
from collections import Counter


NUM_PLAYERS = 2
ROWS = 4


def read_input() -> Tuple[int, List[str]]:
    number_list = []
    n = int(input())
    for _ in range(ROWS):
        number_list.append(input().strip())
    return n, number_list


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
        if val <= k * NUM_PLAYERS:
            points += 1
    return points


k, keyboard = read_input()
print(count_points(k, keyboard))
