# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(plan):
    R = len(plan)
    C = len(plan[0])
    WALL = "#"
    EMPTY = "."
    DIRTY = "*"

    visited = [[False for _ in range(C)] for _ in range(R)]
    robot_runs = 0

    def dfs(r, c):
        visited[r][c] = True
        if plan[r][c] == DIRTY:
            dirty_found[0] = True

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < R
                and 0 <= nc < C
                and not visited[nr][nc]
                and plan[nr][nc] != WALL
            ):
                dfs(nr, nc)

    dirty_found = [False]
    for r in range(R):
        for c in range(C):
            if (plan[r][c] == EMPTY or plan[r][c] == DIRTY) and not visited[r][c]:
                dirty_found = [False]
                dfs(r, c)
                if dirty_found[0]:
                    robot_runs += 1

    return robot_runs


if __name__ == "__main__":
    plan = [
        "###########",
        "#*#.#.....#",
        "#.#...#.#.#",
        "#.#.#.#.#.#",
        "#...#...#*#",
        "###########",
    ]
    # Two separate rooms on the left and right, each with dirty tiles
    # Expected: 2
    print(plan)
    print(solution(plan))
