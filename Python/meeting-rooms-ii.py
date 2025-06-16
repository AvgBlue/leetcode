from collections import deque
from typing import Deque, List
import unittest
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(key=lambda x: x[0])
        min_heap = [intervals[0][1]]

        max_size: int = 1
        for l in intervals[1:]:
            while min_heap and min_heap[0] <= l[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, l[1])
            max_size = max(max_size, len(min_heap))
        return max_size


class TestMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_overlap(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 2)

    def test_no_overlap(self):
        intervals = [[7, 10], [2, 4]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 1)

    def test_all_overlap(self):
        intervals = [[1, 10], [2, 9], [3, 8], [4, 7]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 4)

    def test_empty(self):
        intervals = []
        self.assertEqual(self.solution.minMeetingRooms(intervals), 0)

    def test_one_meeting(self):
        intervals = [[1, 5]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 1)

    def test_back_to_back(self):
        intervals = [[1, 5], [5, 10], [10, 15]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 1)

    def test_complex(self):
        intervals = [[1, 5], [2, 6], [6, 10], [5, 8]]
        self.assertEqual(self.solution.minMeetingRooms(intervals), 2)


if __name__ == "__main__":
    unittest.main()
