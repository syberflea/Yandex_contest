"""
ID 88864381
"""
from collections import deque
from operator import add, sub, floordiv, mul

OPERATORS = {"+": add, "-": sub, "*": mul, "/": floordiv}


class StackLimitException(Exception):
    """Stack is empty."""
    pass


class Stack:
    def __init__(self):
        self._items = deque()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise StackLimitException("getting element from an empty stack") from None

    def __repr__(self):
        return f"Stack({list(self._items)})"


def calc(args):
    stack = Stack()
    for arg in args:
        if arg in OPERATORS:
            op1, op2 = stack.pop(), stack.pop()
            try:
                stack.push(OPERATORS[arg](op2, op1))
            except Exception as error:
                raise ValueError("operation not allowed") from error
        else:
            try:
                stack.push(int(arg))
            except Exception as error:
                raise ValueError("not a digit") from error

    return stack.pop()


def main():
    line = input().split()
    print(calc(line))


if __name__ == "__main__":
    main()
