# Definition for a binary tree node.
from typing import Optional

class TreeNode:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent, node = self.find_node(root, key)

        if node is None:
            return root

        if node.right is None or node.left is None:
            substitute_node = None

            if node.left is not None:
                substitute_node = node.left
            else:
                substitute_node = node.right

            if parent is None:
                return substitute_node
            elif parent.left is node:
                parent.left = substitute_node
            else:
                parent.right = substitute_node

            return root

        min_parent = None
        min_node = node.right

        while min_node.left:
            min_parent = min_node
            min_node = min_node.left

        if min_parent is not None:
            min_parent.left = min_node.right
        else:
            node.right = min_node.right

        node.val = min_node.val
        return root

    def find_node(self, root: Optional[TreeNode], key: int):
        parent = None
        while root and root.val != key:
            parent = root
            if key < root.val:
                root = root.left
            else:
                root = root.right
        return (parent, root)
    