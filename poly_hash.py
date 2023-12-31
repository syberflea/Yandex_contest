from functools import reduce
import time

def evaluate(base, modulo, array):
    if not array:
        return 0
    result = array[-1]
    power = base
    for i in array[-2::-1]:
        result = i * power + result
        power = (power * base) % modulo
    return result % modulo


def calc_hash(base, modulo, array):
    if not array:
        return 0
    result = reduce(lambda x1, x2: x1 * base + x2, array)
    return result % modulo


def calc_hash_2(base, modulo, array):
    k = 0
    n = len(array) - 1
    y = array[n]
    while k != n:
        k += 1
        y = y * base + array[n - k]
    return y % modulo


def main():
    base = int(input())
    modulo = int(input())
    array_of_char = list(map(ord, input()))
    # print(calc_hash(base, modulo, array_of_char))
    # iterations = 100
    # total_time = timeit("calc_hash(base, modulo, array_of_char)", number=100, globals=globals())
    # print(f"Average time is {total_time / iterations:.2f} seconds")
    t1 = time.perf_counter(), time.process_time()
    print(calc_hash(base, modulo, array_of_char))
    t2 = time.perf_counter(), time.process_time()
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")


if __name__ == "__main__":
    main()
