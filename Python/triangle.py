from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        t_len: int = len(triangle)
        for i in range(t_len - 1, 0, -1):
            for j in range(i):
                triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
        return triangle[0][0]



if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    sol = Solution()
    print(sol.minimumTotal(triangle))
