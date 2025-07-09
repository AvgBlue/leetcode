from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head_odd: Optional[ListNode] = ListNode(-1)
        head_even: Optional[ListNode] = ListNode(-1)
        pred_odd = head_odd
        pred_even = head_even
        runner_odd = head
        runner_even = head.next
        while runner_odd and runner_even:
            pred_odd.next = runner_odd
            pred_odd = pred_odd.next

            pred_even.next = runner_even
            pred_even = pred_even.next

            runner_odd = runner_even.next
            runner_even = runner_odd.next if runner_odd else None

        if runner_odd:
            pred_odd.next = runner_odd
            pred_odd = pred_odd.next

        pred_odd.next = head_even.next
        pred_even.next = None
        return head_odd.next


def print_list(node: Optional[ListNode]):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print("->".join(vals))


if __name__ == "__main__":
    # Example: 1->2->3->4->5
    nodes = [ListNode(i) for i in range(1, 6)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    sol = Solution()
    new_head = sol.oddEvenList(head)
    print_list(new_head)
