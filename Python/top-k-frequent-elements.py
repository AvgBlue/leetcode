from typing import Dict, List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict: Dict[int, int] = defaultdict(int)
        for num in nums:
            frequent_dict[num] += 1
        keys: List[int] = list(frequent_dict.keys())
        keys.sort(key=lambda x: frequent_dict[x], reverse=True)
        print(keys)
        return keys[:k]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))
