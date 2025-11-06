from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        len_s = len(s)
        s_set: Set[str] = set([s[0]])
        result = 1

        for end in range(1, len_s):
            while s[end] in s_set:
                s_set.remove(s[start])
                start += 1
            result = max(result, end - start + 1)
            s_set.add(s[end])
        return result


if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
