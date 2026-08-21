from collections import deque
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=deque([nums[0]])
        arr2=deque([nums[1]])
        len_nums=len(nums)
        i=2
        while i<len_nums:
            num=nums[i]
            if arr1[-1]>arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
            i+=1
        return list(arr1)+list(arr2)

        


if __name__ == "__main__":
    solution = Solution()

    examples = [
        ([2, 1, 3], [2, 3, 1]),
        ([5, 4, 3, 8], [5, 3, 4, 8]),
    ]

    for nums, expected in examples:
        result = solution.resultArray(nums)
        print(f"Expected: {expected} | Result: {result}")
