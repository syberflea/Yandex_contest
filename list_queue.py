class Node:
    def __init__(self, value=None, next_elem=None):
        self.value = value
        self.next = next_elem
    def __str__(self):
        return self.value
    def __repr__(self):
        return f"Node(value={self.value}, next_elem={self.next})"


class ListQueue:
    def __init__(self):
        self.queue_size = 0
        self.head = None

    def get(self):
        if self.head is None:
            return 'error'
        previous_node = self.head
        self.head = self.head.next
        self.queue_size -= 1
        return previous_node.value

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def size(self):
        return self.queue_size

    def put(self, value):
        node = Node(value=value)
        if self.head is None:
            self.head = node
            self.queue_size += 1
            return
        for cur_node in self:
            pass
        self.queue_size += 1
        cur_node.next = node


def main():
    cmd_n = int(input())
    queue = ListQueue()
    for _ in range(cmd_n):
        command = input().split()
        if command[0] == 'put':
            queue.put(int(command[1]))
        elif command[0] == 'get':
            print(queue.get())
        elif command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    main()