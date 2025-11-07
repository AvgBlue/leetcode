from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        len_matrix = len(matrix)
        len_len_matrix = len(matrix[0])

        result = [0 for _ in range(len_matrix * len_len_matrix)]
        index = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        index_direction = 0
        vector = (0, 1)
        visited = [[False] * len_len_matrix for _ in range(len_matrix)]
        i = 0
        j = 0
        while index < len_matrix * len_len_matrix:
            print(f"{i} {j}")
            result[index] = matrix[i][j]
            index += 1
            visited[i][j] = True
            i += vector[0]
            j += vector[1]
            if (
                i < 0
                or len_matrix <= i
                or j < 0
                or len_len_matrix <= j
                or True == visited[i][j]
            ):
                i -= vector[0]
                j -= vector[1]
                index_direction = (index_direction + 1) % 4
                vector = directions[index_direction]
                i += vector[0]
                j += vector[1]
        return result


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.spiralOrder(matrix1))

    # Test case 2
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(solution.spiralOrder(matrix2))
