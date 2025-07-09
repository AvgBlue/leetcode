from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)
        memo = {len_nums: 0}

        def runner(index: int):
            if index in memo:
                return memo[index]
            if index >= len_nums:
                return 0
            result = max(nums[index] + runner(index + 2), runner(index + 1))
            memo[index] = result
            return result

        return runner(0)


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))
