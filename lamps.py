# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def tree_pass3(link, value=0):
    if link.left is not None:
        value = (link.value if value < link.value else value)
        value = tree_pass3(link.left, value)
    if link.right is not None:
        value = (link.value if value < link.value else value)
        value = tree_pass3(link.right, value)
    if value < link.value:
        return link.value
    else:
        return value


def solution(root) -> int:
    return tree_pass3(root, root.value)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
