class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums+nums


def run_tests():
    sol = Solution()

    tests = [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([1], [1, 1]),
        ([5, 6], [5, 6, 5, 6]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]),
    ]

    for i, (nums, expected) in enumerate(tests, start=1):
        result = sol.getConcatenation(nums)

        print(f"Test {i}: {nums}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()