# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result: List[List[int]] = []

        curr_level: List[int] = [root]
        next_level: List[int] = []
        rev: bool = False

        this_level: List[int] = []

        while len(curr_level) > 0:
            for node in curr_level:
                if node:
                    this_level.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if rev:
                this_level.reverse()
            if len(this_level) > 0:
                result.append(this_level)
            rev = not rev
            this_level = []

            curr_level = next_level
            next_level = []
        return result
