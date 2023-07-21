"""
функция insert_node(root, key):
  если key < root.key, то
      если root.left == None, то root.left = Node(key)
    иначе insert_node(root.left, key)
  если key >= root.key, то
      если root.right == None, то root.right = Node(key)
    insert_node(root.right, key)
"""
# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

        def __repr__(self):
            return (f"value={self.value} "
                    f"left={self.left.value if self.left else 'None'} "
                    f"right={self.right.value if self.right else 'None'}")


def insert(root, key) -> Node:
    if root is None:
        return Node(value=key)
    if key < root.value:
        if root.left is None:
            root.left = Node(value=key)
        else:
            root.left = insert(root.left, key)
    if key >= root.value:
        if root.right is None:
            root.right = Node(value=key)
        else:
            root.right = insert(root.right, key)
    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()
