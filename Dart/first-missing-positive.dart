class Solution {
  int firstMissingPositive(List<int> nums) {
    int n = nums.length;
    for (int i = 0; i < n; i++) {
    int num =nums[i];
      if (num < 1 || num > n) {
        nums[i] = n + 1;
      }
    }
    for (int i = 0; i < n; i++) {
      int num = nums[i].abs(); 
      if (num <= n) { 
        nums[num - 1] = -nums[num - 1].abs(); 
      }
    }
    for (int i = 0; i < n; i++) {
      if (nums[i] > 0) return i + 1;
    }
    return n + 1;
  }
}
