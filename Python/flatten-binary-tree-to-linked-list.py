# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current_node: Optional[TreeNode] = TreeNode()

        def add_node(node: Optional[TreeNode]) -> None:
            nonlocal current_node
            current_node.right = node
            current_node.left=None
            current_node = node

        def runner(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            left_node = node.left if node.left else None
            right_node = node.right if node.right else None
            add_node(node)
            if left_node:
                runner(left_node)
            if right_node:
                runner(right_node)

        runner(root)
