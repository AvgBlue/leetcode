# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result: Optional[ListNode] = ListNode(-1)
        l1_runner = l1
        l2_runner = l2
        carry: int = 0
        pred = result
        while l1_runner or l2_runner or carry:
            if l1_runner and l2_runner:
                sum = l1_runner.val + l2_runner.val + carry
                l1_runner.val = sum % 10
                carry = sum // 10
                pred.next = l1_runner
                pred = pred.next
                l1_runner = l1_runner.next
                l2_runner = l2_runner.next
                continue
            if l1_runner:
                sum = l1_runner.val + carry
                l1_runner.val = sum % 10
                carry = sum // 10
                pred.next = l1_runner
                pred = pred.next
                l1_runner = l1_runner.next
                continue
            if l2_runner:
                sum = l2_runner.val + carry
                l2_runner.val = sum % 10
                carry = sum // 10
                pred.next = l2_runner
                pred = pred.next
                l2_runner = l2_runner.next
                continue
            if carry:
                pred.next = ListNode(1)
                break

        return result.next


def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))
