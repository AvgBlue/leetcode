from collections import Counter
import random


class Solution:

    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def helper(s1: str, s2: str) -> bool:
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            lenS1: int = len(s1)
            lenS2: int = len(s2)
            if lenS1 != lenS2 or Counter(s1) != Counter(s2):
                memo[(s1, s2)] = False
                return False
            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            if lenS1 == 1:
                memo[(s1, s2)] = s1[0] == s2[0]
                return memo[(s1, s2)]

            for i in range(1, lenS1):
                x1, y1 = s1[:i], s1[i:]
                x2, y2 = s2[:i], s2[i:]
                x2_swap, y2_swap = s2[-i:], s2[:-i]

                result1 = helper(x1, x2) and helper(y1, y2)
                result2 = helper(x1, x2_swap) and helper(y1, y2_swap)

                if result1 or result2:
                    memo[(s1, s2)] = True
                    return True

            memo[(s1, s2)] = False
            return False

        return helper(s1, s2)
    
if __name__ == "__main__":
    solution = Solution()
    s1 = "abcde"
    s2 = "caebd"
    print(f"Is '{s2}' a scrambled string of '{s1}'? {solution.isScramble(s1, s2)}")
