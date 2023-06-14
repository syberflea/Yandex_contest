"""
Помогите Васе написать код функции, вычисляющей y = ax^2 + bx + c. Напишите программу, которая будет по коэффициентам a,
b, c и числу x выводить значение функции в точке x.
"""


def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    return a * (x * x) + (b * x) + c


a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))
