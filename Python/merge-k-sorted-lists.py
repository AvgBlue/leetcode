from typing import List, Optional, Tuple
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head_result = ListNode(-1)
        runner = head_result

        def add(node):
            if not node:
                return
            nonlocal runner
            runner.next = node
            runner = node

        heap: List[Tuple[int, int, ListNode]] = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            _, idx, node = heapq.heappop(heap)
            add(node)
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        add(None)

        return head_result.next

if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def build_list(arr):
        dummy = ListNode(0)
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    # Helper function to print a linked list
    def print_list(node):
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        print("->".join(vals))

    # Example usage
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    sol = Solution()
    merged = sol.mergeKLists(lists)
    print_list(merged)
