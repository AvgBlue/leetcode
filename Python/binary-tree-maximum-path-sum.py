# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum: int = -20000

        def runner(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return -20000
            sum_left = runner(node.left)
            sum_right = runner(node.right)
            max_path_single: int = max(sum_left, sum_right)

        runner(root)
        return max_sum


def build_tree(values):
    """
    Builds a binary tree from a list of values (level-order traversal).
    None values denote missing nodes.
    """
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


if __name__ == "__main__":
    # Example usage:
    # Construct the tree: [1,2,3]
    root = build_tree([1, -2, -3, 1, 3, -2, None, -1])
    sol = Solution()
    print(sol.maxPathSum(root))  # Output: 4
