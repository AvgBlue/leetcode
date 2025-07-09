from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_nums = len(nums)

        def runner(index: int) -> int:
            max_result = 0
            for i in range(index + 1, len_nums):
                if nums[i] > nums[index]:
                    max_result = max(max_result, runner(i))
            return 1 + max_result

        return max(runner(i) for i in range(len_nums))


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    sol = Solution()
    print(sol.lengthOfLIS(nums))
