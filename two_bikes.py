def binarySearch(arr, x, left, right):
    # промежуток пуст
    if right <= left:
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] >= x > arr[mid-1] or mid == 0:
        return mid + 1
    elif x <= arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


def main():
    observation = int(input())
    savings = list(map(int, input().strip().split()))
    bike_price = int(input())
    first_day = binarySearch(savings, bike_price, left=0, right=observation)
    second_day = binarySearch(savings, bike_price*2, left=0, right=observation)
    return first_day, second_day


if __name__ == "__main__":
    print(*main())