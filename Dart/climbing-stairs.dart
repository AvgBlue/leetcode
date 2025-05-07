class Solution {
  int climbStairs(int n) {
    int result = 0;

    List<int> memo = List.filled(n + 1, -1);

    int allWays(int i) {
      if (i > n) return 0;
      if (i == n) return 1;
      if (memo[i] != -1) {
        return memo[i];
      }
      return allWays(i + 1) + allWays(i + 2);
    }

    for (int i = 0; i <= n; i++) {
      memo[n - i] = allWays(n - i);
    }

    result = allWays(0);
    return result;
  }
}

void main() {
  Solution solution = Solution();
  int n = 5; // Example input
  print("Number of ways to climb $n stairs: ${solution.climbStairs(n)}");
}
