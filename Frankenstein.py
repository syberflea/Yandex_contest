from typing import List, Union, Any

a: list[Union[int, Any]] = [677, 591, 153, 356, 617, 337, 195, 948, 440, 657, 631, 546, 148, 678]


def alive(a):
    f = False
    x = a[1]

    for i in range(1, len(a)):
        if (a[i] % 2 == 0) and (f == False):
            x = a[i]
            f = True
        if (a[i] < x) and (a[i] % 2 == 0):
            x = a[i]

    if f == False:
        print(0)
    else:
        print(x)


if __name__ == '__main__':
    alive(a)
