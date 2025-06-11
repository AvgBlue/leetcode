class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from typing import List, Optional


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        next_level: List[Optional[Node]] = []
        curr_level: List[Optional[Node]] = [root]

        while curr_level:

            for i in range(len(curr_level) - 1):
                node: Optional[Node] = curr_level[i]
                next_node: Optional[Node] = curr_level[i + 1]
                node.next = next_node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if curr_level[-1].left:
                next_level.append(curr_level[-1].left)
            if curr_level[-1].right:
                next_level.append(curr_level[-1].right)
            curr_level = next_level
            next_level = []
        return root


if __name__ == "__main__":
    # Example usage:
    # Construct a perfect binary tree:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4  5  6   7
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    root = Node(1, n2, n3)

    sol = Solution()
    sol.connect(root)

    # Print next pointers for each level
    level = root
    while level:
        curr = level
        while curr:
            nxt_val = curr.next.val if curr.next else None
            print(f"{curr.val}->({nxt_val})", end=" ")
            curr = curr.next
        print()
        level = level.left
