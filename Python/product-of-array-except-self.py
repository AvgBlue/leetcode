from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix_mul = [1] + [0] * (len_nums-1)
        for i in range(1, len_nums):
            prefix_mul[i] = prefix_mul[i - 1] * nums[i - 1]
        suffix = 1
        for i in range(len_nums - 1, -1, -1):
            prefix_mul[i] *=  suffix
            suffix *= nums[i]
        prefix_mul
        return prefix_mul


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    result = sol.productExceptSelf(nums)
    print(result)
