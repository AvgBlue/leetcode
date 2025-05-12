# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_int = sys.maxsize
        min_int = -sys.maxsize - 1

        def boundBy(val: int, min: int, max: int) -> bool:
            return min < val and val < max

        def runner(root: Optional[TreeNode], min: int, max: int) -> bool:
            resultLeft: bool = root.left is None
            resultRight: bool = root.right is None
            val: int = root.val
            if not resultLeft:
                left: int = root.left.val
                resultLeft = (
                    left < val
                    and boundBy(left, min, max)
                    and runner(root.left, min, val)
                )
            if not resultRight:
                right: int = root.right.val
                resultRight = (
                    val < right
                    and boundBy(right, min, max)
                    and runner(root.right, val, max)
                )
            return resultLeft and resultRight

        return runner(root, min_int, max_int)