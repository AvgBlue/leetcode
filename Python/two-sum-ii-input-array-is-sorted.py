from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start: int = 0
        end: int = len(numbers) - 1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start, end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
        return []


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(numbers, target)
    print(result)
