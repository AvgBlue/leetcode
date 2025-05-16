# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []

        this_level: List[int] = []

        next_level: List[Optional[TreeNode]] = []
        curr_level: List[Optional[TreeNode]] = [root]

        while len(curr_level) > 0:
            for node in curr_level:
                if node:
                    this_level.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if len(this_level) > 0:
                result.append(this_level)
                this_level = []
            curr_level = next_level
            next_level = []
        result.reverse()
        return result
