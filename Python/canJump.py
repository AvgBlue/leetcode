from typing import Dict, List
from collections import deque



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        last = len(nums) - 1
        for i, step in enumerate(nums):
            if i > farthest:           # can't even reach this index
                return False
            farthest = max(farthest, i + step)
            if farthest >= last:       # can reach (or pass) the end
                return True
        return True


if __name__ == "__main__":
    nums = [2, 0, 0]
    sol = Solution()
    print(sol.canJump(nums))
