from typing import List


class Solution:

    def longestSubsequence(self, nums: List[int]) -> int:
            len_nums=len(nums)
    
            result=0

            xor=0
            is_zero=nums[0]==0
            start,end=0,len_nums
            for num in nums:
                xor^=num
                is_zero^=num==0
            if xor!=0:
                return len_nums
            if not is_zero:
                return len_nums-1
            while is_zero and start<end:
                if nums[start]!=0:
                    return end-start-1
                if nums[end-1]!=0:
                    return end-start-1
                start+=1
                end-=1
            return 0


if __name__ == "__main__":
    sol = Solution()

    examples = [
        [1, 2, 3],
        [2, 3, 4],
        [7,6,1,9],
        [0,0,0,0],
        [5,10,0,15]
    ]

    for nums in examples:
        print(nums, "->", sol.longestSubsequence(nums))
