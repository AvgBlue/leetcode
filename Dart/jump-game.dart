class Solution {
  bool canJump(List<int> nums) {
    int numsSize = nums.length;
    List<bool> canJump = List.filled(numsSize, false);

    canJump[numsSize - 1] = true;
    int minJump = numsSize - 1;
    for (int i = 1; i <= numsSize; i++) {
      if (numsSize - i + nums[numsSize - i] <= minJump) {
        canJump[numsSize - i] = true;
        minJump = numsSize - i;
      }
      else{
        canJump[numsSize - i] = false;
      }
    }

    return canJump[0];
  }
}

void main() {
  Solution solution = Solution();
  
  List<int> nums1 = [2, 3, 1, 1, 4];
  bool result1 = solution.canJump(nums1);
  print(result1); // Output: true

  List<int> nums2 = [3, 2, 1, 0, 4];
  bool result2 = solution.canJump(nums2);
  print(result2); // Output: false
}