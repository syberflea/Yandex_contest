from collections import Counter


def count_sort(n, wardrobe):
    if n < 1:
        return []

    result = []
    cnt = sorted(Counter(wardrobe))
    for num, count in cnt.items():
        for _ in range(count):
            result.append(num)
    return result


def main():
    n = int(input())
    wardrobe = list(map(int, input().strip().split()))
    print(*sorted(wardrobe))


if __name__ == "__main__":
    main()
