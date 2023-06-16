"""
Разложение числа на простые множители.
"""
from typing import List

def factorize(number: int) -> List[int]:
    div = 2
    while number >= div * div:
        if number % div == 0:
            yield div
            number //= div
        else:
            div += 1
    yield number

result = (int(input()))
print(" ".join(map(str, factorize(result))))
