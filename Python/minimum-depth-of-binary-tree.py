# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result: int = 1
        if root is None:
            return 0
        curr_level: List[Optional[TreeNode]] = [root]
        next_level: List[Optional[TreeNode]] = []
        while curr_level:
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                if node.left is None and node.right is None:
                    return result
            result += 1
            curr_level = next_level
            next_level = []
        return result
