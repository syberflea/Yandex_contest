"""
Финальное задание #1:
Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера
домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.
"""
from typing import List, Tuple
ELEM = 0
MAX_HOUSE = 10**9


def split_list(number_list: List[int], val: int):
    print("The original list : " + str(number_list))
    result = []
    temp_list = []
    for n, elem in enumerate(number_list):
        if elem == val:
            temp_list.append(elem)
            result.append(temp_list)
            temp_list = []
        else:
            temp_list.append(elem)
    result.append(temp_list)

    print("The list after splitting by a value : " + str(result))
    return result


def get_nearest_zero_1(street_len: int, number_list: List[int]) -> List[int]:
    distance = []
    zero_position = None
    for i, value in enumerate(number_list):
        if value == 0:
            zero_position = i
            distance.append(0)
            continue
        if zero_position is not None:
            distance.append(i - zero_position)
        else:
            distance.append(street_len)
    return distance


def get_nearest_zero_2(street_len: int, number_list: List[int]) -> List[int]:
    elem_indices = [idx for idx, val in enumerate(number_list) if val == ELEM]
    elems_count = len(elem_indices)
    near_zero_list = []
    if elems_count == 1:
        idx = elem_indices[0]
        if idx == 0:
            # near_zero_list.append(ELEM)
            near_zero_list = [n for n in range(0, street_len)]
        elif idx == street_len-1:
            near_zero_list = [n for n in range(street_len-1, -1, -1)]
            # near_zero_list.append(ELEM)
        else:
            pass
    if elems_count == 2:
        idx_1 = elem_indices[0]
        idx_2 = elem_indices[1]
        if idx_1 == 0 and idx_2 == street_len-1:
            # near_zero_list.append(ELEM)
            near_zero_list = [n for n in range(0, street_len // 2)]
            near_zero_list.extend([n for n in range((street_len//2), -1, -1)])
        else:
            pass
    if elems_count > 2:
        pass
    return near_zero_list


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
print(" ".join(map(str, get_nearest_zero_1(len_street, numbers))))
