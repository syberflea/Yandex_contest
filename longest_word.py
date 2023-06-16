"""
Необходимо оценить сложность статьи: берётся случайное предложение из текста и в нём ищется самое длинное слово.
Его длина и будет условной сложностью статьи.
"""
from collections import Counter
def get_longest_word(line: str) -> str:
    words = line.split()
    word_len = {w: len(w) for w in words}
    cnt = Counter(word_len)
    return cnt.most_common(1)[0][0]

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

line = read_input()
print_result(get_longest_word(line))