# Definition for a binary tree node.
from typing import Dict, List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        memo: Dict[int, int] = {}

        def caculate_height(root: Optional[TreeNode]) -> None:
            if id(root) is None:
                return
            stack1: List[int] = [root]
            stack2: List[int] = []

            while stack1:
                node: Optional[TreeNode] = stack1.pop()
                stack2.append(node)
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)

            while stack2:
                node: Optional[TreeNode] = stack2.pop()
                left_height: int = memo.get(id(node.left), -1)
                right_height: int = memo.get(id(node.left), -1)
                memo[node] = max(left_height, right_height) + 1

        caculate_height(root)

        def runner(root: Optional[TreeNode]):
            if root is None:
                return True
            return (
                abs(memo.get(id(root.left), -1) - memo.get(id(root.right), -1)) <= 1
                and runner(root.left)
                and runner(root.right)
            )

        return runner(root)
