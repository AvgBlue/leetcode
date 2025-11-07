from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        len_board = len(board)
        len_len_board = len(board[0])

        def num_of_neighbors(i: int, j: int) -> int:
            result = 0
            for y in range(max(0, i - 1), min(i + 2, len_board)):
                for x in range(max(0, j - 1), min(j + 2, len_len_board)):
                    if y == i and x == j:
                        continue
                    result += 1 if board[y][x] in [1, -1, -2] else 0
            return result

        for i in range(len_board):
            for j in range(len_len_board):
                result = num_of_neighbors(i, j)
                if result < 2:
                    board[i][j] = -1 if 1 == board[i][j] else 0
                if result == 2:
                    board[i][j] = 1 if 1 == board[i][j] else 0
                if result == 3:
                    board[i][j] = 1 if 1 == board[i][j] else -3
                if 3 < result:
                    board[i][j] = -2 if 1 == board[i][j] else 0
        for i in range(len_board):
            for j in range(len_len_board):
                if -3 == board[i][j]:
                    board[i][j] = 1
                if board[i][j] in [-1, -2]:
                    board[i][j] = 0


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print("before:")
    for a in board:
        print(a)

    solution = Solution()
    solution.gameOfLife(board)

    print("after:")
    for a in board:
        print(a)
