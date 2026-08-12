from collections import Counter
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = {}
        start = 0
        result = 0

        for end, num_end in enumerate(nums):
            counter[num_end] = counter.get(num_end,0)+1

            while counter[num_end] > k:
                num_start = nums[start]
                counter[num_start] -= 1
                start += 1

            current_length = end - start + 1
            if current_length > result:
                result = current_length

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1, 2, 1, 2, 1, 2]
    k = 1

    print(
        "Longest Subarray Length:",
        solution.maxSubarrayLength(nums, k),
    )