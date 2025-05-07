from typing import List

class Solution:
    @staticmethod
    def grayCode(n: int) -> List[int]:
        result = []
        for i in range(1 << n):
            result.append(i ^ (i >> 1))
        return result

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 1. sort so equal elements are adjacent
        nums.sort()
        n = len(nums)
        # 2. generate all Gray codes of length n
        gray_codes = Solution.grayCode(n)
        
        res: List[List[int]] = []
        seen: set = set()
        
        # 3. for each code, build the subset by testing each bit
        for code in gray_codes:
            subset: List[int] = []
            for j in range(n):
                if code & (1 << j):
                    subset.append(nums[j])
            t = tuple(subset)
            # 4. avoid duplicate subsets
            if t not in seen:
                seen.add(t)
                res.append(subset)
        
        return res