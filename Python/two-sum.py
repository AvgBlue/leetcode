from typing import Dict, List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNums: Dict[int, int] = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in mapNums:
                return [mapNums[num2], i]
            mapNums[num1] = i
        return []


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 3]
    target = 6
    print(solution.twoSum(nums, target))
