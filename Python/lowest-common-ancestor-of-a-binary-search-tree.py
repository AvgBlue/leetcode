# Definition for a binary tree node.
from typing import Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # make sure that p<q if not swap them
        if not p.val < q.val:
            p, q = q, p
        node = root
        while node:
            if p.val <= node.val <= q.val:
                return node
            elif node.val < p.val:
                node = node.right
                continue
            if q.val < node.val:
                node = node.left
            else:
                return None
        return None

    def lowestCommonAncestorNotBST(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def runner(node: TreeNode) -> Tuple[TreeNode, bool, bool]:
            if not node:
                return (None, False, False)
            if node == p:
                _, _, is_q1 = runner(node.left)
                if is_q1:
                    return (node, True, True)
                _, _, is_q2 = runner(node.right)
                return (node, True, is_q2)
            if node == q:
                _, is_p1, _ = runner(node.left)
                if is_p1:
                    return (node, True, True)
                _, is_p2, _ = runner(node.right)
                return (node, is_p2, True)
            node1, is_p1, is_q1 = runner(node.left)
            if is_p1 and is_q1:
                return (node1, True, True)
            node2, is_p2, is_q2 = runner(node.right)
            if is_p2 and is_q2:
                return (node2, True, True)
            if (is_p1 or is_p2) and (is_q1 or is_q2):
                return (node, True, True)
            return (None, is_p1 or is_p2, is_q1 or is_q2)

        result, _, _ = runner(root)
        return result


def build_bst_from_list(values):
    """Helper function to build a BST from a level-order list with `None` for missing nodes."""
    if not values:
        return None

    nodes = [TreeNode(x) if x is not None else None for x in values]
    child_index = 1
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if child_index < len(nodes):
                nodes[i].left = nodes[child_index]
                child_index += 1
            if child_index < len(nodes):
                nodes[i].right = nodes[child_index]
                child_index += 1
    return nodes[0], {node.val: node for node in nodes if node is not None}


def main():
    sol = Solution()

    # Example 1
    values = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root, node_map = build_bst_from_list(values)
    p, q = node_map[2], node_map[8]
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of 2 and 8: {lca.val}")  # Expected: 6
    assert lca.val == 6

    # Example 2
    p, q = node_map[2], node_map[4]
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of 2 and 4: {lca.val}")  # Expected: 2
    assert lca.val == 2

    # Example 3
    values = [2, 1]
    root, node_map = build_bst_from_list(values)
    p, q = node_map[2], node_map[1]
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of 2 and 1: {lca.val}")  # Expected: 2
    assert lca.val == 2

    values = [3, 1, 4, None, 2]
    root, node_map = build_bst_from_list(values)
    p, q = node_map[2], node_map[4]
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of 2 and 4: {lca.val}")  # Expected: 3
    assert lca.val == 3


if __name__ == "__main__":
    main()
