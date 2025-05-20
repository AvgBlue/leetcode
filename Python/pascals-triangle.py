from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        result: List[List[int]] = [[1], [1, 1]]
        for i in range(2, numRows):
            new_row: List[int] = [1] + ([0] * (i - 1)) + [1]
            for j in range(1, i):
                new_row[j] = result[i - 1][j-1] + result[i - 1][j]
            result.append(new_row)
        return result


if __name__ == "__main__":
    numRows = 5
    sol = Solution()
    triangle = sol.generate(numRows)
    for row in triangle:
        print(row)
