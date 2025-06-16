from typing import Dict, List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_len: int = len(nums)
        # one element
        if nums_len == 1:
            return 1 if nums[0] == k else 0
        result: int = 0
        sum_dict: Dict[int, int] = defaultdict(int)
        sum_dict[0] = 1
        running_sum: int = 0

        for num in nums:
            running_sum += num
            result += sum_dict[running_sum - k]
            sum_dict[running_sum] += 1
        return result


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    k = 1
    sol = Solution()
    print(f"result = {sol.subarraySum(nums, k)}")
