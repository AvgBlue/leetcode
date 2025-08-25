from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        len_nums = len(nums)
        min_jumps = [0] + [len_nums * 10] * (len_nums - 1)
        for curr, max_jumps in enumerate(nums):
            limit = min(len_nums - 1, curr + max_jumps)
            for next in range(curr + 1, limit + 1):
                min_jumps[next] = min(min_jumps[next], min_jumps[curr] + 1)
        return min_jumps[-1]


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    sol = Solution()
    print(sol.jump(nums))
