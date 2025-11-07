from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        len_matrix = len(matrix)
        for i in range( len_matrix):
            for j in range(i + 1, len_matrix):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len_matrix):
            for j in range(len_matrix // 2):
                matrix[i][j], matrix[i][len_matrix - j - 1] = (
                    matrix[i][len_matrix - j - 1],
                    matrix[i][j],
                )


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original matrix:")
    for row in matrix:
        print(row)
    solution.rotate(matrix)
    print("\nRotated matrix:")
    for row in matrix:
        print(row)
