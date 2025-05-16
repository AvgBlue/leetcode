# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional



class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        last: Optional[TreeNode] = TreeNode(float("-inf"))
        node1: Optional[TreeNode] = None
        node2: Optional[TreeNode] = None

        curr: Optional[TreeNode] = root
        while curr:
            if curr.left is None:
                ###
                node=curr
                if last.val > node.val:
                    if node1 is None:
                        node1 = last
                    node2 = node
                last = node
                ###
                curr = curr.right
            else:
                pred: TreeNode = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    ###
                    node=curr
                    if last.val > node.val:
                        if node1 is None:
                            node1 = last
                        node2 = node
                    last = node
                    ##
                    curr = curr.right

        node1.val, node2.val = node2.val, node1.val


if __name__ == "__main__":
    # Helper function to create a binary tree from a list
    def build_tree(values):
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

    # Helper function to perform in-order traversal and collect values
    def in_order_traversal(root):
        result = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)
        return result

    # Example usage
    values = [3, 1, 4, None, None, 2, 5]  # Larger example tree with swapped nodes
    root = build_tree(values)
    print("Before recovery:", in_order_traversal(root))

    solution = Solution()
    solution.recoverTree(root)

    print("After recovery:", in_order_traversal(root))
