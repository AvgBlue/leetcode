class Solution {
  List<List<int>> insert(List<List<int>> intervals, List<int> newInterval) {
    int findStartIndex(List<List<int>> intervals, int target) {
      int left = 0, right = intervals.length - 1;
      while (left <= right) {
        int mid = (left + right) ~/ 2;
        if (intervals[mid][1] >= target) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }
      return left;
    }

    int findEndIndex(List<List<int>> intervals, int target) {
      int left = 0, right = intervals.length - 1;
      while (left <= right) {
        int mid = (left + right) ~/ 2;
        if (intervals[mid][0] <= target) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
      return right;
    }

    void mergeInPlace(List<List<int>> intervals, int startIndex, int endIndex, List<int> newInterval) {
      int start = newInterval[0];
      int end = newInterval[1];

      if (startIndex < intervals.length) {
        start = start < intervals[startIndex][0] ? start : intervals[startIndex][0];
      }
      if (endIndex >= 0) {
        end = end > intervals[endIndex][1] ? end : intervals[endIndex][1];
      }

      // Remove the overlapping intervals
      intervals.removeRange(startIndex, endIndex + 1);

      // Insert the merged interval
      intervals.insert(startIndex, [start, end]);
    }

    int startIndex = findStartIndex(intervals, newInterval[0]);
    int endIndex = findEndIndex(intervals, newInterval[1]);

    // No overlap case
    if (startIndex > endIndex) {
      intervals.insert(startIndex, newInterval);
    } else {
      mergeInPlace(intervals, startIndex, endIndex, newInterval);
    }

    return intervals;
  }
}

