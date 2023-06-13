"""
В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 105
Во второй строке через пробел записаны n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 103.
В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.
"""
from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(arr[0:window_size])
    result.append(current_sum / window_size)
    for i in range(0, len(arr) - window_size + 1):
        current_sum -= arr[i]
        if i + window_size < len(arr):
            current_sum += arr[i + window_size]
            current_avg = current_sum / window_size
            result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))