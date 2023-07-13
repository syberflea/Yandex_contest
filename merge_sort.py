def merge(arr, lf, mid, rg):
    result = []
    left = arr[lf:mid]
    right = arr[mid:rg]
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array, lf, rg):
    if rg - lf >= 2:
        midpoint = (lf + rg) // 2
        merge_sort(array, lf, midpoint),
        merge_sort(array, midpoint, rg)
        array[lf:rg] = merge(array, lf, midpoint, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
