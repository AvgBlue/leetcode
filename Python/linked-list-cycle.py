from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast=head
        slow=head
        while fast.next is not None and fast.next.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast ==slow:
                return True
        return False
            




def build_list(values, pos):
    if not values:
        return None

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


def run_tests():
    s = Solution()

    print("Test 1")
    head = build_list([3, 2, 0, -4], 1)
    assert s.hasCycle(head) is True
    print("Passed")

    print("Test 2")
    head = build_list([1, 2], 0)
    assert s.hasCycle(head) is True
    print("Passed")

    print("Test 3")
    head = build_list([1], -1)
    assert s.hasCycle(head) is False
    print("Passed")

    print("Test 4")
    head = build_list([1], 0)
    assert s.hasCycle(head) is True
    print("Passed")

    print("Test 5")
    head = build_list([1, 2, 3, 4, 5], -1)
    assert s.hasCycle(head) is False
    print("Passed")

    print("Test 6")
    head = build_list([1, 2, 3, 4, 5], 2)
    assert s.hasCycle(head) is True
    print("Passed")

    print("Test 7")
    head = build_list([], -1)
    assert s.hasCycle(head) is False
    print("Passed")

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()