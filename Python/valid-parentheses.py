from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        parentheses_pair={'(':')','[':']','{':'}'}
        for c in s:
            if c in ['(','[','{']:
                stack.append(parentheses_pair[c])
            elif stack and stack[-1]==c:
                stack.pop()
            else:
                return False
        return not stack
            


def run_tests():
    sol = Solution()

    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((()))", True),
        ("((())", False),
        ("(){[()]}", True),
    ]

    for i, (s, expected) in enumerate(tests, start=1):
        result = sol.isValid(s)

        print(f"Test {i}: {s!r}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()