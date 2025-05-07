# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result: Optional[ListNode] = ListNode(-1)
        runner: Optional[ListNode] = head
        while runner is not None:
            node = runner
            runner = runner.next
            node.next = None
            next: Optional[ListNode] = result.next
            result.next = node
            node.next = next
        return result.next

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        newHead=ListNode(-1,head)
        runnerLeft: Optional[ListNode] = newHead
        for i in range(left - 1):
            runnerLeft = runnerLeft.next
        runnerRight: Optional[ListNode] = newHead
        for i in range(right):
            runnerRight = runnerRight.next
        runnerRightNext=runnerRight.next
        runnerRight.next=None
        
        result: Optional[ListNode] = ListNode(-1,runnerRightNext)
        runner: Optional[ListNode] = runnerLeft.next
        while runner is not None:
            node = runner
            runner = runner.next
            node.next = None
            next: Optional[ListNode] = result.next
            result.next = node
            node.next = next
        runnerLeft.next=result.next
        return newHead.next


if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Helper function to convert a linked list to a list
    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    # Example usage
    values = [1, 2, 3,4]
    left, right = 1, 4
    head = create_linked_list(values)

    solution = Solution()
    result = solution.reverseBetween(head, left, right)

    print(linked_list_to_list(result))
