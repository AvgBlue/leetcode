import 'dart:math';

class Solution {
  int maxArea(List<int> height) {
    int result = 0;
    int left = 0;
    int right = height.length - 1;
    while (left < right) {
      result = max(result, min(height[left], height[right]) * (right - left));
      if (height[left] > height[right]) {
        right--;
      } else {
        left++;
      }
    }
    return result;
  }

  int area(List<int> height, int i, int j) {
    return min(height[i], height[j]) * (j - i);
  }
}
