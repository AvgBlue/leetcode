class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        result=-1
        is_move=False

        for i,num in enumerate(nums):
            if i!=num:
                result&=num
                is_move=True
        return result if is_move else 0


def run_tests():
    sol = Solution()

    tests = [
        ([0, 3, 2, 1], 1),
        ([0, 1, 3, 2], 2),
        ([3, 2, 1, 0], 0),
        ([0, 1, 2, 3], 0),
        ([0], 0),
        ([1, 0], 0),
        ([0, 2, 1, 3], 0),
    ]

    for i, (nums, expected) in enumerate(tests, start=1):
        result = sol.sortPermutation(nums)

        print(f"Test {i}: {nums}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()