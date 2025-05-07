import 'dart:math';

class IntervalPart implements Comparable<IntervalPart> {
  final int index;
  final int value;
  final bool isStart;

  IntervalPart(this.index, this.value, this.isStart);

  @override
  int compareTo(IntervalPart other) {
    if (value != other.value) {
      return value.compareTo(other.value);
    } else {
      return isStart == other.isStart ? 0 : (isStart ? -1 : 1);
    }
  }
}


class Solution {
  List<List<int>> merge(List<List<int>> intervals) {
    int length = intervals.length;
    if (length == 1) return intervals;
    List<List<int>> result = [];
    List<IntervalPart> intervalsPartList = List.generate(
        length * 2,
        (int index) => IntervalPart(
            index ~/ 2, intervals[index ~/ 2][index % 2], index % 2 == 0));
    intervalsPartList.sort();

    int stack = 1;
    List<int> interval = [intervalsPartList[0].value];

    for (int i = 1; i < length * 2; i++) {
      if (intervalsPartList[i].isStart) {
        stack++;
      } else {
        stack=max(stack-1,0);
      }
      if (stack == 0) {
        interval.add(intervalsPartList[i].value);
        result.add(interval);
        if (i != 2 * length - 1) {
          interval = [intervalsPartList[i + 1].value];
          stack = 1;
          i++;
        }
      }
    }
    return result;
  }
}


