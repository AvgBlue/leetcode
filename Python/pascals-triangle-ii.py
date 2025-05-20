from typing import List
import math


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [math.comb(rowIndex, i) for i in range(rowIndex + 1)]

    def getRowdp(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1]
        elif rowIndex == 2:
            return [1, 1]
        result: List[int] = [1, 1]
        for i in range(2, rowIndex):
            new_row: List[int] = [1] + ([0] * (i - 1)) + [1]
            for j in range(1, i):
                new_row[j] = result[j - 1] + result[j]
            result = new_row
        return result


if __name__ == "__main__":
    rowIndex = 5
    sol = Solution()
    print(sol.getRow(rowIndex))
