# Python3 program to find closest 0
# for every element

# Print the distance with zeroes of
# every element
def print_distance(arr, n):
    # initializes an array of size n with 0
    ans = [0 for i in range(n)]

    # if first element is 0 then the
    # distance will be 0
    if (arr[0] == 0):
        ans[0] = 0
    else:
        ans[0] = 10 ** 9  # if not 0 then initialize
    # with a maximum value

    # traverse in loop from 1 to n and
    # store the distance from left
    for i in range(1, n):

        # add 1 to the distance from
        # previous one
        ans[i] = ans[i - 1] + 1

        # if the present element is 0 then
        # distance will be 0
        if (arr[i] == 0):
            ans[i] = 0

    # if last element is zero then it will be 0
    # else let the answer be what was found when
    # traveled from left to right
    if (arr[n - 1] == 0):
        ans[n - 1] = 0

    # traverse from right to left and store
    # the minimum of distance if found from
    # right to left or left to right
    for i in range(n - 2, -1, -1):

        # store the minimum of distance from
        # left to right or right to left
        ans[i] = min(ans[i], ans[i + 1] + 1)

        # if it is 0 then minimum will
        # always be 0
        if (arr[i] == 0):
            ans[i] = 0

    return ans


def read_input():
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return n, number_list


len_street, numbers = read_input()
print(" ".join(map(str, print_distance(numbers, len_street))))
