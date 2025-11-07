from collections import defaultdict
from typing import Counter, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict: dict[str, List[str]] = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            result_dict[sorted_s].append(s)
        return list(result_dict.values())


if __name__ == "__main__":
    solution = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped_anagrams = solution.groupAnagrams(input_strs)
    print(grouped_anagrams)
