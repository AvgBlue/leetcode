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
    
    def sortList(self, head: ListNode) -> ListNode:
        # Base case
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # Cut the list

        # Step 2: Sort each half recursively
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach remaining nodes
        tail.next = l1 or l2
        return dummy.next
    
    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.deleteDuplicates(self.sortList(head))
        
        
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

    # Helper function to print a linked list
    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(" -> ".join(map(str, values)))

    # Example usage
    values = [4, 2, 1, 3, 2, 4, 1]
    head = create_linked_list(values)
    print("Original list:")
    print_linked_list(head)

    solution = Solution()
    result = solution.deleteDuplicatesUnsorted(head)

    print("List after removing duplicates:")
    print_linked_list(result)
