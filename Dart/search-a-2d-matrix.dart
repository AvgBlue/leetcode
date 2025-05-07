class Solution {
  int binarySearch<T>(List<T> list, int target, int Function(T, int) compare) {
    int left = 0, right = list.length - 1;

    while (left <= right) {
      int mid = left + (right - left) ~/ 2;
      int cmp = compare(list[mid], target);

      if (cmp == 0) {
        return mid; // Found, return index
      } else if (cmp < 0) {
        left = mid + 1; // Search right half
      } else {
        right = mid - 1; // Search left half
      }
    }
    return -1; // Not found
  }

  int compare1(List<int> l1, int num) {
    if (l1.first <= num && num <= l1.last) return 0;
    if (l1.last < num) return -1;
    return 1;
  }

  int compare2(int n1, int n2) {
    return n1.compareTo(n2);
  }

  bool searchMatrix(List<List<int>> matrix, int target) {
    int row = binarySearch(matrix, target, compare1);
    if (row == -1) {
      return false;
    }
    return -1 != binarySearch(matrix[row], target, compare2);
  }
}
