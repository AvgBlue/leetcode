from typing import List
import math


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return Solution.combine2(n, k, 1)

    @staticmethod
    def combine2(n: int, k: int, start: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(start, n + 1)]
        combNum: int = math.comb(n - start + 1, k)
        result: List[List[int]] = []
        listcomb: List[List[int]] = Solution.combine2(n, k - 1, start + 1)
        for i in range(start, n + 1):
            for l in listcomb:
                if i not in l and i < l[0]:
                    result.append([i] + l)
                    combNum = combNum - 1
                if combNum == 0:
                    return result
        return result


if __name__ == "__main__":
    sol = Solution()
    n = 12
    k = 4
    print(sol.combine(n, k))
