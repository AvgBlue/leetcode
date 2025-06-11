from typing import List, Set, Tuple


D


if __name__ == "__main__":
    board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    Solution().solve(board)
    for row in board:
        print(" ".join(row))
