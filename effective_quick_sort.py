"""
ID 89091591
"""
from dataclasses import dataclass


@dataclass
class Competitor:
    login: str
    score: int
    fine: int

    def __repr__(self):
        return f"{self.__class__.__name__}({self.login}, {self.score}, {self.fine})"

    def __str__(self):
        return f"{self.login} {self.score} {self.fine}"

    def __lt__(self, other):
        return (-self.score, self.fine, self.login) < (-other.score, other.fine, other.login)

    def __le__(self, other):
        return (-self.score, self.fine, self.login) < (-other.score, other.fine, other.login)


def quick_sort2(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [elem for elem in array[1:] if elem <= pivot]
    greater = [elem for elem in array[1:] if elem > pivot]
    return quick_sort2(less) + pivot + quick_sort2(greater)


def partition(array, lo, hi):
    pivot = array[(lo + hi) // 2]
    i = lo
    j = hi - 1
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def quicksort(array, lo, hi):
    if lo < hi:
        pivot = partition(array, lo, hi)
        quicksort(array, lo, pivot)
        quicksort(array, pivot + 1, hi)


def main():
    n_participants = int(input())
    participants = []
    for _ in range(n_participants):
        login, score, fine = input().split()
        c = Competitor(login, int(score), int(fine))
        participants.append(c)
    quicksort(participants, 0, n_participants)
    print("\n".join([everyone.login for everyone in participants]))


if __name__ == '__main__':
    main()
