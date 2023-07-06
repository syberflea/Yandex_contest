class Deque:
    def __init__(self, max_size: int) -> None:
        self._deque = [None] * max_size
        self._max_size = max_size
        self._head = 0
        self._tail = 0
        self._size = 0

    def is_empty(self) -> bool:
        """Check size of list."""
        return self._size == 0

    def push_front(self, item: int) -> None:
        """Add element in start list."""
        if self._size == self._max_size:
            return "error"
        if self.is_empty():
            self._tail = (self._tail + 1) % self._max_size
        self._deque[self._head] = item
        self._head = (self._head - 1) % self._max_size
        self._size += 1

    def push_back(self, item: int) -> None:
        """Add element in end list."""
        if self._size == self._max_size:
            return "error"
        if self.is_empty():
            self._head = (self._head - 1) % self._max_size
        self._deque[self._tail] = item
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1

    def pop_back(self) -> int:
        """Pick an item from the ending of the list."""
        if self.is_empty():
            return "error"
        self._tail = (self._tail - 1) % self._max_size
        item = self._deque[self._tail]
        self._deque[self._tail] = None
        self._size -= 1
        if self._size == 0:
            self._tail = 0
            self._head = 0
        return item

    def pop_front(self) -> int:
        """Pick an item from the beginning of the list."""
        if self.is_empty():
            return "error"
        self._head = (self._head + 1) % self._max_size
        item = self._deque[self._head]
        self._deque[self._head] = None
        self._size -= 1
        if self._size == 0:
            self._tail = 0
            self._head = 0
        return item


def main():
    cmd_n = int(input())
    deque_size = int(input())
    deque = Deque(deque_size)
    for _ in range(cmd_n):
        command = input().split()
        if command[0] == 'push_front':
            deque.push_front(int(command[1]))
        if command[0] == 'push_back':
            deque.push_back(int(command[1]))
        elif command[0] == 'pop_front':
            print(deque.pop_front())
        elif command[0] == 'pop_back':
            print(deque.pop_back())


if __name__ == '__main__':
    main()