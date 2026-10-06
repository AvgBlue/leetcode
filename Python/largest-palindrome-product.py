from math import ceil


class Solution:
    def largestPalindrome(self, n: int) -> int:
        range_start = 10 ** (n - 1)
        range_end = 10 ** n
        range_high = range_end - 1
        for op in [None, -2]:

            for i in range(range_high, range_start - 1, -1):
                str_i = str(i)
                palindrome = int(str_i + str_i[op::-1])

                start_j = max(
                    range_start,
                    ceil(palindrome / range_high)
                )

                end_j = min(
                    range_high,
                    palindrome // range_start
                )

                for j in range(start_j, end_j + 1):
                    if palindrome % j == 0:
                        return palindrome % 1337

        return 0


def run_tests():
    sol = Solution()

    tests = [
        (1, 9),
        (2, 987),
        (3, 123),
        (4, 597),
        (5, 677),
        (6, 1218),
        (7, 877),
        (8, 475),
    ]
    for i, (n, expected) in enumerate(tests, start=1):
        result = sol.largestPalindrome(n)

        print(f"Test {i}: n = {n}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()