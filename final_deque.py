"""
ID 88866234
"""
from operator import attrgetter

from exceptions import DequeTopLimitException, DequeLowLimitException

COMMANDS = {
    "push_back": "push_back",
    "push_front": "push_front",
    "pop_front": "pop_front",
    "pop_back": "pop_back"
}


class Deque:
    def __init__(self, n):
        self.__buffer = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size == self.max_n:
            raise DequeTopLimitException("deque is full")
        if self.is_empty():
            self.head = (self.head - 1) % self.max_n
        self.__buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_n:
            raise DequeTopLimitException("deque is full")
        if self.is_empty():
            self.tail = (self.tail + 1) % self.max_n
        self.__buffer[self.head] = value
        self.head = (self.head - 1) % self.max_n
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise DequeLowLimitException("deque is empty")
        self.head = (self.head + 1) % self.max_n
        head_value = self.__buffer[self.head]
        self.__buffer[self.head] = None
        self.size -= 1
        if self.size == 0:
            self.head = self.tail = 0
        return head_value

    def pop_back(self):
        if self.is_empty():
            raise DequeLowLimitException("deque is empty")
        self.tail = (self.tail - 1) % self.max_n
        tail_value = self.__buffer[self.tail]
        self.__buffer[self.tail] = None
        self.size -= 1
        if self.size == 0:
            self.head = self.tail = 0
        return tail_value


def main():
    cmd_n = int(input())
    deque_size = int(input())
    deque = Deque(deque_size)
    for _ in range(cmd_n):
        command, *args = input().split()
        try:
            result = attrgetter(COMMANDS[command])(deque)(*args)
            if result:
                print(result)
        except DequeTopLimitException:
            print("error")
        except DequeLowLimitException:
            print("error")


if __name__ == '__main__':
    main()
