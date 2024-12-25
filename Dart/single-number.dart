class Solution {
  int singleNumber(List<int> nums) {
    Map<int, bool> map = Map();
    for (int i = 0; i < nums.length; i++) {
      if (map.containsKey(nums[i])) {
        map[nums[i]] = true;
        continue;
      }
      map[nums[i]] = false;
    }
    for (int i = 0; i < nums.length; i++) {
      if (!map[nums[i]]!) {
        return nums[i];
      }
    }
    return 0;
  }
}
