class Solution {
  List<List<int>> fourSum(List<int> nums, int target) {
    List<List<int>> result = [];
    nums.sort();
    
    return result;
  }

  List<List<int>> threeSum(List<int> nums, int target) {
    List<List<int>> result = [];
    nums.sort();
    int n = nums.length - 2;
    for (int i = 0; i < n; i++) {
      if (nums[i] > 0) break;

      if (i > 0 && nums[i] == nums[i - 1]) continue;

      int left = i + 1;
      int right = nums.length - 1;

      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];

        if (sum == target) {
          result.add([nums[i], nums[left], nums[right]]);

          int leftVal = nums[left];
          while (left < right && nums[left] == leftVal) {
            left++;
          }

          int rightVal = nums[right];
          while (left < right && nums[right] == rightVal) {
            right--;
          }
        } else if (sum < target) {
          left++;
        } else {
          right--;
        }
      }
    }

    return result;
  }
}
