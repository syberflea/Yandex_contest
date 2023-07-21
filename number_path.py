# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

        def __repr__(self):
            return (f"value={self.value} "
                    f"left={self.left.value if self.left else 'None'} "
                    f"right={self.right.value if self.right else 'None'}")


def solution(root, cur_sum=0) -> int:
    if root is None:
        return 0
    cur_sum = cur_sum * 10 + root.value
    if root.left is None and root.right is None:
        return cur_sum
    return solution(root.left, cur_sum) + solution(root.right, cur_sum)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == '__main__':
    test()
