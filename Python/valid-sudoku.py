from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        box_counter = [[False] * 9 for _ in range(9)]
        row_counter = [[False] * 9 for _ in range(9)]
        col_counter = [[False] * 9 for _ in range(9)]


        for i in range(9):
            for j in range(9):
                if "." != board[i][j]:
                    number = int(board[i][j]) - 1
                    if (
                        box_counter[j // 3 + 3 * (i // 3)][number]
                        or row_counter[i][number]
                        or col_counter[j][number]
                    ):
                        return False
                    box_counter[j // 3 + 3 * (i // 3)][number] = True
                    row_counter[i][number] = True
                    col_counter[j][number] = True
        return True


if __name__ == "__main__":
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(solution.isValidSudoku(board))
