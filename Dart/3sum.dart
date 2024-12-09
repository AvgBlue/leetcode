class Solution {
  List<List<int>> threeSum(List<int> nums) {
    List<List<int>> result = [];
    nums.sort();
    int n = nums.length - 2;
    for (int i = 0; i < nums.length - 2; i++) {
      if (nums[i] > 0) break;

      if (i > 0 && nums[i] == nums[i - 1]) continue;

      int left = i + 1;
      int right = nums.length - 1;

      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];

        if (sum == 0) {
          result.add([nums[i], nums[left], nums[right]]);

          // Move left pointer forward and skip duplicates
          int leftVal = nums[left];
          while (left < right && nums[left] == leftVal) {
            left++;
          }

          // Move right pointer backward and skip duplicates
          int rightVal = nums[right];
          while (left < right && nums[right] == rightVal) {
            right--;
          }
        } else if (sum < 0) {
          // If sum is too small, move the left pointer to increase the sum.
          left++;
        } else {
          // If sum is too large, move the right pointer to decrease the sum.
          right--;
        }
      }
    }

    return result;
  }
}
