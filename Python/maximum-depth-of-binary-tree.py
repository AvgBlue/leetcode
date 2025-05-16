# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        result: int = 0
        curr_level: List[int] = [root]
        next_level: List[int] = []
        while len(curr_level) > 0:
            for node in curr_level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
            if len(next_level) > 0:
                result += 1
            curr_level = next_level
            next_level = []
        return result
