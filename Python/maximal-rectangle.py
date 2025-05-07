from typing import List
'''
[["1","0","1","0","0"]
,["1","0","1","1","1"]
,["1","1","1","1","1"]
,["1","0","0","1","0"]]

[["1","0","1","0","0"]
,["2","0","2","1","1"]
,["3","1","3","2","2"]
,["4","0","0","3","0"]]
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        maxArea = 0

        for row in matrix:
            for j in range(cols):
                # Update the running height
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))

        return maxArea

    
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea: int = 0
        heights.append(0)
        stack: List[int] = []
        # we go over the heights
        for i in range(len(heights)):
            while len(stack) != 0 and heights[i] < heights[stack[-1]]:
                # caculate the area where the pop element is the smallest element
                height: int = heights[stack.pop()]
                width: int = i
                if len(stack) != 0:
                    width = i - stack[-1] - 1
                area: int = height * width
                maxArea = max(maxArea, area)
            stack.append(i)

        return maxArea
    
    
if __name__ == "__main__":
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print("Maximal Rectangle Area:", solution.maximalRectangle(matrix))