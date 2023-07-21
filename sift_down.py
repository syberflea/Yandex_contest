def sift_down(heap, idx) -> int:
    left = 2 * idx
    right = 2 * idx + 1
    heap_size = len(heap)-1
    if heap_size < left:
        return idx
    if right <= heap_size and heap[right] > heap[left]:
        index_largest = right
    else:
        index_largest = left
    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
