from collections import defaultdict
from typing import Dict, List


class Solution:
    def frequencySort(self, s: str) -> str:
        # step 1
        freq: Dict[str, int] = defaultdict(int)
        for c in s:
            freq[c] += 1
        # step 2
        buckets: Dict[int, List[str]] = defaultdict(list)
        for c, val in freq.items():
            buckets[val].append(c)
        # step 3
        result_parts: List[str] = []
        for val in sorted(buckets.keys(), reverse=True):
            for c in buckets[val]:
                result_parts.append(c * val)
        return "".join(result_parts)


if __name__ == "__main__":
    sol = Solution()
    # Example usage for frequencySort
    s = "loveleetcode"
    print("Sorted by frequency:", sol.frequencySort(s))
