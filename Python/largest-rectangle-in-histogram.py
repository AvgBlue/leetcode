from typing import List


class Solution:
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
    histogram = [2, 1, 5, 6, 2, 3]
    print("Largest Rectangle Area:", solution.largestRectangleArea(histogram))