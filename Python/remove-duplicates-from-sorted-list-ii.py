# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getNext(head: Optional[ListNode]) -> Optional[ListNode]:
            while(True):
                node: Optional[ListNode] = head
                if head is None or head.next is None or head.val != head.next.val:
                    return head
                if node.val == node.next.val:
                    num: int = node.val
                    while node is not None and node.val == num:
                        node = node.next
                    head=node

        newHead: Optional[ListNode] = ListNode(-1, head)
        runner: Optional[ListNode] = newHead
        while runner is not None:
            node: Optional[ListNode] = getNext(runner.next)
            runner.next = node
            runner = runner.next
        return newHead.next


if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
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
    values = [1, 2, 3, 3, 4, 4, 5]
    head = create_linked_list(values)
    solution = Solution()
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
