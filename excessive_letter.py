"""
Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием букв строки s и добавлением 1
буквы в случайную позицию. Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. Строки не бывают
пустыми.

Формат вывода
Выведите лишнюю букву.
"""
from typing import Tuple
from collections import Counter

def get_excessive_letter(shorter: str, longer: str) -> str:
    return list((Counter(longer) - Counter(shorter)).keys())[0]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
