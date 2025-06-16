from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        result: List[List[int]] = [intervals[0]]

        for l in intervals[1:]:
            current = result[-1]
            if current[0] <= l[0] <= current[1]:
                if current[1] < l[1]:
                    current[1] = l[1]
            else:
                result.append(l)
        return result


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    sol = Solution()
    result = sol.merge(intervals)
    print(result)
