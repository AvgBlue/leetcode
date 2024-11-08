class Solution {
  List<int> twoSum(List<int> nums, int target) {
    Map<int, int> numToIndex = {};
    for (int i = 0; i < nums.length; i++) {
      int comploment = target - nums[i];
      if (numToIndex.containsKey(comploment)) {
        return [numToIndex[comploment]!, i];
      }
      numToIndex[nums[i]] = i;
    }
    return [-1, -1];
  }
}

void main() {
  Solution solution = Solution();
  List<int> result = solution.twoSum([3, 2, 4], 6);
  print(result);
}
