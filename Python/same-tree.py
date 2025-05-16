# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isP: bool = p is None
        isQ: bool = q is None
        if isP and isQ:
            return True
        if isP != isQ:
            return False
        if (
            p.val != q.val
            or not self.isSameTree(p.left, q.left)
            or not self.isSameTree(p.right, q.right)
        ):
            return False
        return True
