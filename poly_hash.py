from functools import reduce


def evaluate(base, modulo, array):
    if not array:
        return 0
    result = ord(array[-1])
    power = base
    for i in array[-2::-1]:
        result = ord(i) * power + result
        power = (power * base) % modulo
    return result % modulo


def horner_hash(base, modulo, array):
    if not array:
        return 0

    result = reduce(lambda x1, x2: x1 * base + x2, map(ord, array))
    return result % modulo


def main():
    base = int(input())
    modulo = int(input())
    array_of_char = input()
    print(horner_hash(base, modulo, array_of_char))


if __name__ == "__main__":
    main()
