from typing import List


class Solution:

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:

        result=0
        len_y=len(grid)
        len_x=len(grid[0])
        table=[[0]*len_x for _ in range(len_y)]
        num_map={'X':1,'Y':-1,'.':0}
        valid_map={'X':True,'Y':True,'.':False}

        valid_table=[[False]*len_x for _ in range(len_y)]

        for i in range(len_y):
            for j in range(len_x):
                table[i][j] = num_map[grid[i][j]]
                valid_table[i][j] = valid_map[grid[i][j]]

                if j > 0:
                    table[i][j] += table[i][j - 1]
                    valid_table[i][j] |= valid_table[i][j - 1]

        for j in range(len_x):
            for i in range(1,len_y):
                table[i][j]+=table[i-1][j]
                valid_table[i][j]|=valid_table[i-1][j]

        for i in range(len_y):
            for j in range(len_x):
                if valid_table[i][j] and table[i][j]==0:
                        result+=1

        return result


if __name__ == "__main__":
    solution = Solution()

    examples = [
        ([['X', 'Y', '.'], ['Y', '.', '.']], 3),
        ([['X', 'X'], ['X', 'Y']], 0),
        ([['.', '.'], ['.', '.']], 0),
        ([['X','Y','X'],['.','.','.'],['.','.','Y']],4)
    ]

    for grid, expected in examples:
        result = solution.numberOfSubmatrices(grid)
        print(f"Grid: {grid} | Expected: {expected} | Result: {result}")
