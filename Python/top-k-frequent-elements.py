from typing import Dict, List
from collections import defaultdict


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            len_nums=len(nums)
            frequent_dict: Dict[int, int] = defaultdict(int)
            for num in nums:
                frequent_dict[num] += 1
            buckets: Dict[int, List[int]] = defaultdict(list)

            for num, freq in frequent_dict.items():
                buckets[freq].append(num)
            
            result=[]
            len_result=0

            for freq in sorted(buckets.keys(), reverse=True):
                bucket=buckets[freq]
                if len(bucket)+len_result<k:
                    result+=bucket
                    len_result+=len(bucket)
                else:
                    result+=bucket[0:k-len_result]
                    return result
            return result


if __name__ == "__main__":
    nums = [5,3,1,1,1,3,73,1]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))
