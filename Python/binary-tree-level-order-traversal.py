from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result: List[List[int]] = []

        tree_list: List[Optional[int]] = []
        curr_list: List[Optional[TreeNode]] = [root]
        next_level: List[Optional[TreeNode]] = []
        while len(curr_list) > 0:
            for node in curr_list:
                if node:
                    tree_list.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if len(tree_list) > 0:
                result.append(tree_list)
            curr_list = next_level
            next_level = []
            tree_list = []
        return result


if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree: [3,9,20,None,None,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print("start")
    sol = Solution()
    print(sol.levelOrder(root))
