# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

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


def tree_pass(link, value):
    if link is None:
        return True
    if link.left is not None:
        tree_pass(link.left, value)
        if value > link.value:
            return False
    if link.right is not None:
        tree_pass(link.right, value)
        if value < link.value:
            return False
    return True


def pre_order(node):
    if not node:
        return
    print(node.value, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def solution2(root) -> bool:
    # current_value = root.value
    # if root.left:
    #     if root.left.value >= current_value or not solution(root.left):
    #         return False
    # if root.right:
    #     if root.right.value <= current_value or not solution(root.right):
    #         return False
    return True


def solution(node, min_value=float('-inf'), max_value=float('inf')):
    if node is None:
        return True
    if node.value <= min_value or max_value <= node.value:
        return False
    return (
            solution(node.left, min_value, node.value)
            and solution(node.right, node.value, max_value)
    )


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
