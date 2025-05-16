# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums_len = len(nums)
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid: int = nums_len // 2
        root: Optional[TreeNode] = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root


if __name__ == "__main__":

    def preorder_traversal(root):
        if not root:
            return []
        return (
            [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)
        )

    nums = [-10, -3, 0, 5, 9]
    sol = Solution()
    bst_root = sol.sortedArrayToBST(nums)
    print("Preorder traversal of BST:", preorder_traversal(bst_root))
