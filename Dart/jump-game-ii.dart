import 'dart:math';
class Solution {
  int jump(List<int> nums) {
    int jumps = 0;
    int currentEnd = 0; 
    int farthest = 0;  

    for (int i = 0; i < nums.length - 1; i++) {
      farthest = max(farthest, i + nums[i]);

      
      if (i == currentEnd) {
        jumps++;
        currentEnd = farthest;

        if (currentEnd >= nums.length - 1)break;
      }
    }

    return jumps;
  }
}
