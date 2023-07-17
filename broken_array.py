"""
ID 89009319
"""
def broken_search(nums, target) -> int:
    low = 0
    high = len(nums) - 1
    n = len(nums)

    while low <= high:
        mid = (low + high) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


def main():
    array_len = int(input())
    number = int(input())
    array = list(map(int, input().strip().split()))
    print(broken_search(array, number))


if __name__ == "__main__":
    test()
