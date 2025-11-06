from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_nums = len(nums)
        min_size = len_nums + 2
        start = 0
        end = 0
        window_sum = nums[start]

        while end < len_nums:
            if window_sum == target:
                min_size = min(end - start + 1, min_size)
                end += 1
                if end < len_nums:
                    window_sum += nums[end]
                continue
            if window_sum < target:
                end += 1
                if end < len_nums:
                    window_sum += nums[end]
                continue
            if target < window_sum:
                min_size = min(end - start + 1, min_size)
                if start == end:
                    start += 1
                    end = start
                    if end < len_nums:
                        window_sum = nums[end]
                else:
                    window_sum -= nums[start]
                    start += 1
        if min_size == len_nums + 2:
            return 0
        return min_size


if __name__ == "__main__":
    target = 11
    nums = [1, 2, 3, 4, 5]
    sol = Solution()
    result = sol.minSubArrayLen(target, nums)
    print(result)
