from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        runner=head
        seen = set()
        while runner is not None:
            if runner in seen:
                return runner
            seen.add(runner)
            runner=runner.next
        return None



def build_list(values, pos):
    if not values:
        return None, None

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    cycle_start = None

    if pos != -1:
        nodes[-1].next = nodes[pos]
        cycle_start = nodes[pos]

    return nodes[0], cycle_start


def run_tests():
    s = Solution()

    print("Test 1")
    head, expected = build_list([3, 2, 0, -4], 1)
    result = s.detectCycle(head)

    assert result is expected
    print("Passed")


    print("Test 2")
    head, expected = build_list([1, 2], 0)
    result = s.detectCycle(head)

    assert result is expected
    print("Passed")


    print("Test 3")
    head, expected = build_list([1], -1)
    result = s.detectCycle(head)

    assert result is None
    print("Passed")


    print("Test 4")
    head, expected = build_list([1], 0)
    result = s.detectCycle(head)

    assert result is expected
    print("Passed")


    print("Test 5")
    head, expected = build_list([1, 2, 3, 4, 5], 2)
    result = s.detectCycle(head)

    assert result is expected
    print("Passed")


    print("Test 6")
    head, expected = build_list([1, 2, 3, 4, 5], -1)
    result = s.detectCycle(head)

    assert result is None
    print("Passed")


    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()