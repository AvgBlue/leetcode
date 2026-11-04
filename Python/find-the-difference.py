from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        num=0
        for c in s:
            num^=ord(c)
        for c in t:
            num^=ord(c)
        return chr(num)



def run_tests():
    sol = Solution()

    tests = [
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
        ("a", "aa", "a"),
        ("ae", "aea", "a"),
        ("xyz", "xzyq", "q"),
        ("aaaa", "aaaaa", "a"),
    ]

    failed = 0

    for i, (s, t, expected) in enumerate(tests, start=1):
        result = sol.findTheDifference(s, t)

        print(f"Test {i}")
        print(f"s:        {s!r}")
        print(f"t:        {t!r}")
        print(f"result:   {result!r}")
        print(f"expected: {expected!r}")

        if result == expected:
            print("Passed\n")
        else:
            print("FAILED\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()