from typing import List, Optional


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


class Solution:
    def connect(self, root: Node) -> Node:
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
                    next_level.append(node.right)
            if curr_level[-1].left:
                next_level.append(curr_level[-1].left)
                next_level.append(curr_level[-1].right)
            curr_level = next_level
            next_level = []
        return root
