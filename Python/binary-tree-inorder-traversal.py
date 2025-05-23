# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []

        def runner(node: Optional[TreeNode]):
            if node is None:
                return
            runner(node.left)
            result.append(node.val)
            runner(node.right)

        runner(root)
        return result
