from typing import Dict, List, Set, Tuple, Optional


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set: Set[Tuple[int, int, int]] = set()
        result_list: List[int] = []

        def twoSum(target: int, skip: int):
            nonlocal nums, result_set
            left, right = 0, len(nums) - 1
            while left < right:
                if right == skip:
                    right -= 1
                    continue
                if left == skip:
                    left += 1
                    continue
                sum = nums[left] + nums[right]
                if sum == target:
                    l: List[int] = [-target, nums[left], nums[right]]
                    l.sort()
                    result_set.add((l[0], l[1], l[2]))
                    left += 1
                    right -= 1
                if sum > target:
                    right -= 1
                    if right == skip:
                        right -= 1
                elif sum < target:
                    left += 1

        nums.sort()
        prev: Optional[int] = None
        for i, num in enumerate(nums):
            if prev is not None and prev == num:
                continue
            twoSum(-num, i)
            prev = num

        for s in result_set:
            result_list.append(list(s))
        return result_list


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -1, -4]
    sol = Solution()
    print(sol.threeSum(nums))
