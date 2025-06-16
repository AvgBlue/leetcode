from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1:
            return nums
        result: List[int] = []
        d_q = deque() 

        for i, num in enumerate(nums):
            if d_q and d_q[0] <= i - k:
                d_q.popleft()
            while d_q and nums[d_q[-1]] < num:
                d_q.pop()
            d_q.append(i)
            if i >= k - 1:
                result.append(nums[d_q[0]])
        return result


if __name__ == "__main__":
    nums = [1, 3, 1, 2, 0, 5]
    k = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))
