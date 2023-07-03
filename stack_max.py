class StackMax:
    def __init__(self):
        self.items = []
        self.max_item = 0

    def push(self, item):
        self.items.append(item)
        self.max_item = max(self.items)

    def pop(self):
        if self.size() > 0:
            elem = self.items.pop()
            self.max_item = max(self.items, default=0)
            return elem
        else:
            self.max_item = 0
            return "error"

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.size() > 0:
            self.max_item = max(self.items, default=0)
            return self.max_item
        else:
            return "None"


def main():
    stack = StackMax()
    n = int(input())
    result = []
    for index in range(n):
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')
        if command[0] == 'get_max':
            result.append(stack.get_max())
    for index in result:
        print(index)


if __name__ == '__main__':
    main()
