
class Solution:

    def orangesRotting(self, grid: list[list[int]]) -> int:
        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        
        m=len(grid)
        n=len(grid[0])

        fresh_orange_count=0
        

        def inbound(pos):
            return 0<=pos[0]<m and 0<=pos[1]<n

        def add_pos(pos1,pos2):
            return (pos1[0]+pos2[0],pos1[1]+pos2[1])

        def get_grid(pos):
            return grid[pos[0]][pos[1]]

        def set_grid(pos,val):
            grid[pos[0]][pos[1]]=val

        def corrupt(pos):
            nonlocal fresh_orange_count

            result=[]
            
            for direction in directions:
                new_pos=add_pos(pos,direction)
                if inbound(new_pos) and get_grid(new_pos)==1:
                    set_grid(new_pos,2)
                    fresh_orange_count-=1
                    result.append(new_pos)
            return result

        
                    

        this_level=[]

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh_orange_count+=1
                elif grid[i][j]==2:
                    this_level.append((i,j))

                    
        next_level=[]
        minute_count=0
        is_change=False
        while this_level:
            for pos in this_level:
                next_level+=corrupt(pos)
            this_level=next_level
            next_level=[]
            minute_count+=1
            is_change=True
        if is_change:
            minute_count-=1

        return minute_count if fresh_orange_count==0 else -1


def run_tests():
    sol = Solution()

    tests = [
        (
            [
                [2, 1, 1],
                [1, 1, 0],
                [0, 1, 1],
            ],
            4,
        ),
        (
            [
                [2, 1, 1],
                [0, 1, 1],
                [1, 0, 1],
            ],
            -1,
        ),
        (
            [[0, 2]],
            0,
        ),
        (
            [[1]],
            -1,
        ),
        (
            [[2]],
            0,
        ),
        (
            [
                [2, 1],
                [1, 1],
            ],
            2,
        ),
        (
            [
                [2, 0, 1],
            ],
            -1,
        ),
        ([[0]],0),
    ]

    for i, (grid, expected) in enumerate(tests, start=1):
        # Copy because your solution may mutate the grid
        test_grid = [row[:] for row in grid]

        result = sol.orangesRotting(test_grid)

        print(f"Test {i}")
        print(f"grid:     {grid}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()