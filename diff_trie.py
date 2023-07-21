def tree_count(n):
    if n >= 2:
        c = ((2 * ((2 * n) - 1)) / (n + 1)) * tree_count(n - 1)
        return int(c)
    return 1


def main():
    n = int(input().strip())
    print(tree_count(n))


if __name__ == '__main__':
    main()
