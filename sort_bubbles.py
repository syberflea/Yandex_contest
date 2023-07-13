def sort(array, length):
    already_sorted = True
    for i in range(length):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = True
        if already_sorted:
            print(*array)
            already_sorted = False


def sort2(array, length):
    i = 0
    t = True
    while t:
        t = False
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                t = True
        i = i + 1


def main():
    length = int(input())
    array = list(map(int, input().strip().split()))
    sort(array, length)


if __name__ == "__main__":
    main()
