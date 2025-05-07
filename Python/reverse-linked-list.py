# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result:Optional[ListNode] = ListNode(-1)
        runner:Optional[ListNode] = head
        while(runner is not None):
            node=runner
            runner=runner.next
            node.next=None
            next: Optional[ListNode] = result.next
            result.next = node
            node.next = next
        return result.next
        
            
            
            
