# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def runner(start: int, end: int) -> Optional[TreeNode]:
            nums_len = end - start
            if nums_len < 1:
                return None
            if nums_len == 1:
                return TreeNode(nums[start])
            mid: int = start + (nums_len // 2)
            root: Optional[TreeNode] = TreeNode(nums[mid])
            root.left = runner(start, mid)
            root.right = runner(mid + 1, end)
            return root

        return runner(0, len(nums))


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
