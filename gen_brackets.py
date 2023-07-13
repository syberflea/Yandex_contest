
def gen(n: int, counter_open: int, counter_close: int, ans: str):
    if counter_open + counter_close == 2 * n:
        print(ans)
        return
    if counter_open < n:
        gen(n, counter_open + 1, counter_close, ans + '(')
    if counter_open > counter_close:
        gen(n, counter_open, counter_close + 1, ans + ')')


def main():
    len_seq = int(input())
    start = 0
    stop = 0
    prefix = ''
    gen(len_seq, start, stop, prefix)


if __name__ == "__main__":
    main()
