class Solution {
  final Map<int, List<String>> memo = {};

  List<String> generateParenthesis(int n) {
    if (memo.containsKey(n)) {
      return memo[n]!;
    }

    List<String> result = [];

    void backtrack(String current, int open, int close) {
      if (current.length == 2 * n) {
        result.add(current);
        return;
      }

      if (open < n) {
        backtrack(current + '(', open + 1, close);
      }

      if (close < open) {
        backtrack(current + ')', open, close + 1);
      }
    }

    backtrack('', 0, 0);
    memo[n] = result;
    return result;
  }
}
