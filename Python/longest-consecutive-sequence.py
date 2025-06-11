from typing import Set


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        s: Set = set(nums)
        result: int = 1
        for num in s:
            if num - 1 not in s:
                curr: int = 1
                runner: int = num
                while runner + 1 in s:
                    runner = runner + 1
                    curr += 1
                result = max(result, curr)
        return result


if __name__ == "__main__":
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    sol = Solution()
    print(sol.longestConsecutive(nums))
