import re

class Solution:
    def checkString(self, s: str) -> bool:
        return bool(re.fullmatch(r"a*b*", s)) 


def run_tests():
    sol = Solution()

    tests = [
        ("aaabbb", True),
        ("abab", False),
        ("bbb", True),
        ("aaa", True),
        ("a", True),
        ("b", True),
        ("ab", True),
        ("ba", False),
        ("aababb", False),
        ("aaaaabbbbb", True),
    ]

    failed = 0

    for i, (s, expected) in enumerate(tests, start=1):
        result = sol.checkString(s)

        print(
            f"Test {i}: s={s!r}, "
            f"result={result}, expected={expected}"
        )

        if result == expected:
            print("Passed\n")
        else:
            print("FAILED\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()