from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        len_nums: int = len(nums)

        def backtrack(start: int):
            nonlocal result, len_nums
            if start == len_nums:
                result.append(nums[:])
                return
            for i in range(start, len_nums):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))
