def merge_sort2(array):
    if len(array) == 1:  # базовый случай рекурсии
        return array

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: len(array) // 2])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[len(array) // 2: len(array)])

    # заводим массив для результата сортировки
    result = [] * len(array)

    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1


def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:])
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A


def main():
    gardners = int(input())
    beds_list = [
        # "".join(input().strip().split())
        list(map(int, input().strip().split()))
        for _ in range(gardners)
    ]
    # print(beds_list)
    sorted_beds = sorted(beds_list)
    # print(*sorted_beds)
    result = []
    idx = 0
    start, end = sorted_beds[0]
    idx += 1

    while idx < gardners:
        if start <= sorted_beds[idx][0] <= end:
            _, curr_end = sorted_beds[idx]
            idx += 1
            if curr_end > end:
                end = curr_end
        else:
            result.append([start, end])
            start, end = sorted_beds[idx]
            idx += 1
    result.append([start, end])
    for each in result:
        print(*each)


if __name__ == "__main__":
    main()
