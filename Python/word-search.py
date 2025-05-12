from typing import List, Tuple


class Marker:
    board: List[List[str]]
    stack: List[Tuple[int, int, str]]

    def __init__(self, board: List[List[str]]):
        self.board = board
        self.stack = []

    def mark(self, location: Tuple[int, int]):
        x, y = location
        c: str = self.board[x][y]
        self.stack.append((x, y, c))
        self.board[x][y] = "*"

    def unmark(self):
        x, y, c = self.stack.pop()
        self.board[x][y] = c

    def unmarkItimes(self, times: int):
        for _ in range(times):
            if self.stack:
                x, y, c = self.stack.pop()
                self.board[x][y] = c


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def runner(location: Tuple[int, int], index: int) -> bool:
            nextStep: List[Tuple[int, int]] = []
            steps: int = 0
            while True:
                marker.mark(location)
                steps = steps + 1
                if index == wordLen:
                    return True
                x, y = location
                nextStep: List[Tuple[int, int]] = []
                if (
                    (0 < x)
                    and (board[x - 1][y] != "*")
                    and (board[x - 1][y] == word[index])
                ):  # Up
                    nextStep.append((x - 1, y))
                if (
                    (x + 1 < m)
                    and (board[x + 1][y] != "*")
                    and (board[x + 1][y] == word[index])
                ):  # Down
                    nextStep.append((x + 1, y))
                if (
                    (0 < y)
                    and (board[x][y - 1] != "*")
                    and (board[x][y - 1] == word[index])
                ):  # Left
                    nextStep.append((x, y - 1))
                if (
                    (y + 1 < n)
                    and (board[x][y + 1] != "*")
                    and (board[x][y + 1] == word[index])
                ):  # Right
                    nextStep.append((x, y + 1))
                if len(nextStep) == 0:
                    marker.unmarkItimes(steps)
                    return False
                if len(nextStep) == 1:
                    location = nextStep[0]
                    index = index + 1
                    continue
                break
            for nextLocation in nextStep:
                if runner(nextLocation, index + 1):
                    return True
            marker.unmarkItimes(steps)
            return False

        m: int = len(board)
        n: int = len(board[0])
        wordLen: int = len(word)
        marker: Marker = Marker(board)
        for i in range(m):
            if word[0] in board[i]:
                for j in range(n):
                    if board[i][j] == word[0] and runner((i, j), 1):
                        return True
        return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    solution = Solution()
    print(solution.exist(board, word))  # Output: True
