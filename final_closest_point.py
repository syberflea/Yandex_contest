"""
ID: 88414942
"""
from typing import List, Tuple
ELEM = 0
MAX_HOUSE = 10**9


def get_nearest_zero(street_len: int, number_list: List[int]) -> List[int]:
    near_zero_list = [0 for i in range(street_len)]

    if number_list[0] == 0:
        near_zero_list[0] = 0
    else:
        near_zero_list[0] = MAX_HOUSE

    for i in range(1, street_len):
        near_zero_list[i] = near_zero_list[i - 1] + 1
        if number_list[i] == 0:
            near_zero_list[i] = 0

    if number_list[street_len - 1] == 0:
        near_zero_list[street_len - 1] = 0

    for i in range(street_len - 2, -1, -1):
        near_zero_list[i] = min(near_zero_list[i], near_zero_list[i + 1] + 1)
        if number_list[i] == 0:
            near_zero_list[i] = 0
    return near_zero_list


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return n, number_list


len_street, numbers = read_input()
print(" ".join(map(str, get_nearest_zero(len_street, numbers))))
