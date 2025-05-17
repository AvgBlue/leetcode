# Definition for singly-linked list.
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_middle_node(
            node: Optional[ListNode],
        ) -> Tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
            slow = node
            fast = node
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
                next_mid = slow.next if slow else None
            if prev:
                prev.next = None
            return (prev, slow, next_mid)

        def runner(head: Optional[ListNode]) -> Optional[TreeNode]:
            if head is None:
                return None
            if head.next is None:
                return TreeNode(head.val)
            prev_mid_node, mid_node, next_mid_node = find_middle_node(head)
            prev_mid_node.next, mid_node.next = None, None
            root: Optional[TreeNode] = TreeNode(mid_node.val)
            root.left = runner(head)
            root.right = runner(next_mid_node)
            return root

        return runner(head)
