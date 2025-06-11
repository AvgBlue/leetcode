from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        next_level: List[Optional[TreeNode]] = []
        curr_level: List[Optional[TreeNode]] = [root]
        sum: int = 0
        while curr_level:
            for node in curr_level:
                childs: List[Optional[TreeNode]] = []
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
                if childs:
                    for child in childs:
                        child.val += node.val * 10
                        next_level.append(child)
                else:
                    sum += node.val
            curr_level = next_level
            next_level = []
        return sum


if __name__ == "__main__":
    # Example: [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    sol = Solution()
    print(sol.sumNumbers(root))  # Output: 25
