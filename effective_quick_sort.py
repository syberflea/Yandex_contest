def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [elem for elem in array[1:] if elem <= pivot]
    greater = [elem for elem in array[1:] if elem > pivot]
    return quick_sort(less) + pivot + quick_sort(greater)


def main():
    n_participants = int(input())
    participants = [
        dict(
            zip(
                ['login', 'score', 'fine'],
                input().strip().split()
            )
        )
        for _ in range(n_participants)
    ]
    data_sorted = sorted(participants, key=lambda x: (x["score"], x["fine"]), reverse=True)
    print(*data_sorted)


if __name__ == '__main__':
    main()
