class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        len_intervals=len(intervals)
        result=0
        intervals.sort(key=lambda l:l[1])
        index=0
        for i in range(1,len_intervals):
            if intervals[index][1]<=intervals[i][0]:
                index=i
            else:
                result+=1
        return result


def run_tests():
    s = Solution()

    print("Test 1")
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    assert s.eraseOverlapIntervals(intervals) == 1
    print("Passed")

    print("Test 2")
    intervals = [[1,2],[1,2],[1,2]]
    assert s.eraseOverlapIntervals(intervals) == 2
    print("Passed")

    print("Test 3")
    intervals = [[1,2],[2,3]]
    assert s.eraseOverlapIntervals(intervals) == 0
    print("Passed")

    print("Test 4")
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    assert s.eraseOverlapIntervals(intervals) == 2
    print("Passed")

    print("Test 5")
    intervals = [[-50,-40],[-30,-20],[-10,0]]
    assert s.eraseOverlapIntervals(intervals) == 0
    print("Passed")

    print("Test 6")
    intervals = [[1,5],[2,3],[3,4]]
    assert s.eraseOverlapIntervals(intervals) == 1
    print("Passed")

    print("Test 7")
    intervals = [[1,4],[2,5],[3,6],[7,8]]
    assert s.eraseOverlapIntervals(intervals) == 2
    print("Passed")

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()