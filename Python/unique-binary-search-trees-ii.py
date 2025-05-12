# Definition for a binary tree node.
from typing import List, Optional
from itertools import product


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        def preorder(node):
            if not node:
                return "None"
            left = preorder(node.left)
            right = preorder(node.right)
            return f"{node.val}, {left}, {right}"

        return preorder(self)


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def gen(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            result: List[Optional[TreeNode]] = []
            for root in range(start, end + 1):
                leftList: List[Optional[TreeNode]] = gen(start, root - 1)
                rightList: List[Optional[TreeNode]] = gen(root + 1, end)
                for l in leftList:
                    for r in rightList:
                        result.append(TreeNode(root, l, r))
            return result

        return gen(1, n)


if __name__ == "__main__":
    solution = Solution()
    result = solution.generateTrees(3)
    for tree in result:
        print(tree)
