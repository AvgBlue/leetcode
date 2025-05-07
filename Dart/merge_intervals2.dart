import 'dart:math';

class Solution {
  List<List<int>> merge(List<List<int>> intervals) {
    int length = intervals.length;
    if (length == 1) return intervals;
    List<List<int>> result = [];
    intervals.sort((a, b) => a[0].compareTo(b[0]));
    int start = intervals[0][0];
    int end = intervals[0][1];
    int i = 1;
    for (; i < length; i++) {
      if (start <= intervals[i][0] && intervals[i][0] <= end) {
        end = max(end, intervals[i][1]);
      } else {
        result.add([start, end]);
        start = intervals[i][0];
        end = intervals[i][1];
      }
    }
    result.add([start, end]);
    return result;
  }
}
