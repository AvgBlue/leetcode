class Solution {
  int longestValidParentheses(String s) {
    int result = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == ')') continue;
      int max = 0;
      int stack = 0;
      for (int j = i; j < s.length; j++) {
        if ('(' == s[j]) {
          stack++;
          max++;
          continue;
        }
        if (0 == stack) {
          break;
        }
        stack--;
        max++;
        if (0 == stack && result < max) {
          i = j + 1;
          result = max;
        }
      }
    }
    return result;
  }
}

void main() {
  Solution solution = Solution();
  print(solution.longestValidParentheses("(())(")); // Output: 4
  print(solution.longestValidParentheses(")()())")); // Output: 4
  print(solution.longestValidParentheses("")); // Output: 0
}
