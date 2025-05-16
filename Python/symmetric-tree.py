# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_palindrome(arr: List[int]) -> bool:
            if len(arr) < 1:
                return True
            left, right = 0, len(arr) - 1
            while left < right:
                if arr[left] is None and arr[right] is None:
                    left += 1
                    right -= 1
                    continue
                if arr[left] is None or arr[right] is None:
                    return False
                if arr[left].val != arr[right].val:
                    return False
                left += 1
                right -= 1
            return True

        if root is None:
            return True
        tree_list: List[Optional[int]] = []
        curr_list: List[Optional[TreeNode]] = [root]
        next_level: List[Optional[TreeNode]] = []
        while len(curr_list) > 0:
            for node in curr_list:
                if node:
                    tree_list.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    tree_list.append(None)

            curr_list = next_level
            if not is_palindrome(curr_list):
                return False
            next_level = []
        return True


if __name__ == "__main__":
    # Example usage:
    # Construct a symmetric tree:
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    sol = Solution()
    print(sol.isSymmetric(root))  # Expected output: True
