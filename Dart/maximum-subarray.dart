import 'dart:math';

class Solution {
  int maxSubArray(List<int> nums) {
    int length = nums.length;
    int result = nums[0];
    int now = nums[0];
    for (int i = 0; i < length; i++) {
      now = max(nums[i], now + nums[i]);
      if (result < now) result = now;
    }
    return result;
  }
}
