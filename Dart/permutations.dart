class Solution {
  List<List<int>> permute(List<int> nums) {
    List<List<int>> result = [];
    int length = nums.length;
    void backtrack(int start) {
      if (start == length) {
        result.add(List.from(nums));
      }
      for (int i = start; i < length; i++) {
        swap(nums, start, i);
        backtrack(start + 1);
        swap(nums, start, i);
      }
    }

    backtrack(0);
    return result;
  }

  void swap(List<int> nums, int a, int b) {
    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
  }
}

void main() {
  Solution solution = Solution();
  List<int> nums = [1, 2, 3];
  List<List<int>> permutations = solution.permute(nums);
  print(permutations);
}
