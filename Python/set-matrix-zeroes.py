from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        len_matrix = len(matrix)
        len_len_matrix = len(matrix[0])

        row_to_set = set()
        col_to_set = set()

        for i in range(len_matrix):
            for j in range(len_len_matrix):
                if matrix[i][j] == 0:
                    row_to_set.add(i)
                    col_to_set.add(j)
        for i in row_to_set:
            for j in range(len_len_matrix):
                matrix[i][j] = 0
        for i in col_to_set:
            for j in range(len_matrix):
                matrix[j][i] = 0


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(matrix)
    print(matrix)
