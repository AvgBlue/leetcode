from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid_next_quenn(l: List[int]) -> List[int]:
            options: List[bool] = [True] * n
            curr_row: int = len(l)
            for row, col in enumerate(l):
                # Mark the same column as invalid
                options[col] = False
                # Mark the diagonals as invalid
                diag1 = col + (curr_row - row)
                diag2 = col - (curr_row - row)
                if 0 <= diag1 < n:
                    options[diag1] = False
                if 0 <= diag2 < n:
                    options[diag2] = False
            result: List[int] = []
            for i, b in enumerate(options):
                if b:
                    result.append(i)
            return result

        if n == 1:
            return [["Q"]]
        result: List[List[str]] = []
        curr_level: List[List[int]] = [[i] for i in range(n)]
        next_level = []
        while curr_level:
            for l in curr_level:
                options: List[int] = valid_next_quenn(l)
                for col in options:
                    borad: List[int] = l[:] + [col]
                    if len(borad) == n:
                        result.append(borad)
                    else:
                        next_level.append(borad)
            curr_level = next_level
            next_level = []

        def build_board(path: List[int]) -> List[str]:
            board = []
            for col in path:
                row = ["."] * len(path)
                row[col] = "Q"
                board.append("".join(row))
            return board

        return [build_board(l) for l in result]
if __name__ == "__main__":
    n = 19
    solution = Solution()
    results = solution.solveNQueens(n)
    for board in results:
        for row in board:
            print(row)
        print()