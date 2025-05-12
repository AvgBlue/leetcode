# Definition for a binary tree node.
from typing import List, Optional, Dict
import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def numTrees(self, n: int) -> int:
        memo: Dict[int, int] = {0: 1, 1: 1}

        def c(n: int) -> int:
            if n in memo:
                return memo[n]
            sum: int = 0
            for i in range(n):
                sum += c(i) * c(n - 1 - i)
                memo[n] = sum
            return sum

        for i in range(n):
            c(i)
        return c(n)


if __name__ == "__main__":
    solution = Solution()
    result = {}
    for n in range(1, 20):
        start_time = time.time()
        result[n] = solution.numTrees(n)
        end_time = time.time()
        print(f"Time for n={n}: {end_time - start_time:.6f} seconds")

    print(result)
