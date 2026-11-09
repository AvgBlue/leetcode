from typing import Optional

class Solution:

    def countServers(self, grid: list[list[int]]) -> int:
            len_grid=len(grid)
            len_grid_0=len(grid[0])
            row_to_column=[-1]*len_grid
            counter_column=[0]*len_grid_0
            server_count=0
    
            for i in range(len_grid):
                for j in range(len_grid_0):
                    is_server=grid[i][j]
                    server_count+=is_server
                    counter_column[j]+=is_server
                    if is_server:
                        if row_to_column[i]==-1:
                            row_to_column[i]=j
                        else:
                            row_to_column[i]=None
    
            alone_count=0
            for i in range(len_grid):
                if row_to_column[i] is not None and row_to_column[i]!=-1:
                    alone_count+=(counter_column[row_to_column[i]]==1)
            return server_count-alone_count


    def countServers2(self, grid: list[list[int]]) -> int:
        len_grid=len(grid)
        len_grid_0=len(grid[0])
        counter_row=[0]*len_grid
        counter_column=[0]*len_grid_0

        server_count=0

        for i in range(len_grid):
            for j in range(len_grid_0):
                is_server=grid[i][j]
                server_count+=is_server
                counter_row[i]+=is_server
                counter_column[j]+=is_server

        alone_count=0
        for i in range(len_grid):
            if counter_row[i]==1:
                for j in range(len_grid_0):
                    alone_count+=grid[i][j]*(counter_column[j]==1)
        return server_count-alone_count




def run_tests():
    sol = Solution()

    tests = [
        (
            [
                [1, 0],
                [0, 1],
            ],
            0,
        ),
        (
            [
                [1, 0],
                [1, 1],
            ],
            3,
        ),
        (
            [
                [1, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ],
            4,
        ),
        (
            [
                [1],
            ],
            0,
        ),
        (
            [
                [1, 1, 1],
            ],
            3,
        ),
        (
            [
                [1],
                [1],
                [1],
            ],
            3,
        ),
    ]

    failed = 0

    for i, (grid, expected) in enumerate(tests, start=1):
        test_grid = [row[:] for row in grid]

        result = sol.countServers(test_grid)

        print(f"Test {i}")
        print("grid:")
        for row in grid:
            print(row)

        print(f"result:   {result}")
        print(f"expected: {expected}")

        if result == expected:
            print("Passed\n")
        else:
            print("FAILED\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()