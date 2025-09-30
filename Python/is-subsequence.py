class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s, len_s = 0, len(s)
        for c in t:
            if index_s < len_s and s[index_s] == c:
                index_s += 1
        return index_s == len_s
