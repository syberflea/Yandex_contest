class StackMax:
    def __init__(self):
        self.items = []
        self.max_item = []

    def push(self, item):
        if self.size() == 0 or item >= self.max_item[-1]:
            self.max_item.append(item)
        self.items.append(item)

    def pop(self):
        if self.size() > 0:
            elem = self.items.pop()
            if elem == self.max_item[-1]:
                self.max_item.pop()
            return elem
        else:
            self.max_item.clear()
            return "error"

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.size() > 0:
            return self.max_item[-1]
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
    for each in result:
        print(each)


if __name__ == '__main__':
    main()
