from functools import cmp_to_key


def compare_numbers(a, b):
    num1 = str(a)
    num2 = str(b)
    return int(num1 + num2) - int(num2 + num1)


def find_max_num(arr):
    arr.sort(key=cmp_to_key(compare_numbers), reverse=True)
    largest_num_str = ''.join(map(str, arr))
    return int(largest_num_str)


def main():
    length = int(input())
    array = list(map(int, input().strip().split()))
    print(find_max_num(array))


if __name__ == "__main__":
    main()
