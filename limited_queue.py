MAX_SIZE = 5_000


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.my_size = 0

    def is_empty(self):
        return self.my_size == 0

    def push(self, elem):
        if self.my_size != self.max_n:
            self.queue[self.tail] = elem
        else:
            return "error"
        self.tail = (self.tail + 1) % self.max_n
        self.my_size += 1

    def pop(self):
        if self.is_empty():
            return "None"
        elem = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.my_size -= 1
        return elem

    def size(self):
        return self.my_size

    def peek(self):
        if self.my_size > 0:
            return self.queue[self.head]
        else:
            return "None"


def main():
    cmd_n = int(input())
    size_queue = int(input())
    queue = MyQueueSized(size_queue)
    result = []
    for index in range(cmd_n):
        command = input().split()
        if command[0] == 'push':
            if queue.push(int(command[1])) == 'error':
                result.append('error')
        if command[0] == 'pop':
            result.append(queue.pop())
        if command[0] == 'size':
            result.append(queue.size())
        if command[0] == 'peek':
            result.append(queue.peek())
    for each in result:
        print(each)


if __name__ == '__main__':
    main()
