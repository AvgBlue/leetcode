from typing import Dict
import time


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Len: int = len(s1)
        s2Len: int = len(s2)
        s3Len: int = len(s3)
        if s1Len + s2Len != s3Len:
            return False
        memo: Dict[tuple[int, int], bool] = {}

        def runner(i1: int, i2: int) -> bool:
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            if i1 + i2 == s3Len:
                return True
            result1: bool = False
            result2: bool = False
            if i1 < s1Len:
                is1: bool = s1[i1] == s3[i1 + i2]
                if is1:
                    result1 = runner(i1 + 1, i2)
            if i2 < s2Len:
                is2: bool = s2[i2] == s3[i1 + i2]
                if is2:
                    result2 = runner(i1, i2 + 1)
            memo[(i1, i2)] = result1 or result2
            return result1 or result2

        return runner(0, 0)


if __name__ == "__main__":
    s1 = "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
    s2 = "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
    s3 = "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"
    s1Len: int = len(s1)
    s2Len: int = len(s2)
    s3Len: int = len(s3)
    print(f"len(s1) + len(s2): {s1Len + s2Len}, len(s3): {s3Len}")
    solution = Solution()

    start_time = time.time()
    print(solution.isInterleave(s1, s2, s3))  # Example usage
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
