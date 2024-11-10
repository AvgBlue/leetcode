import 'dart:math';

class Solution {
  int lengthOfLongestSubstring(String s) {
    int maxSubString = 0;
    Set<String> set = Set();
    int start = 0, end = 0;
    while (end < s.length) {
      if (!set.contains(s[end])) {
        set.add(s[end]);
        maxSubString = max(maxSubString, set.length);
        end++;
      } else {
        while (s[start] != s[end]) {
          set.remove(s[start]);
          start++;
        }
        set.remove(s[start]);
        start++;
      }
    }
    return maxSubString;
  }
}

void main() {
  Solution solution = Solution();
  String testString = "abcbb";
  int result = solution.lengthOfLongestSubstring(testString);
  print(
      "The length of the longest substring without repeating characters is: $result");
}
