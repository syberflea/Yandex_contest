# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def height(root) -> int:
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def solution(root) -> bool:
    if root is None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) <= 1 and solution(root.left) and solution(root.right):
        return True
    return False


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()