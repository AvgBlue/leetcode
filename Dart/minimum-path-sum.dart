import 'dart:math';

class Solution {
  int minPathSum(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    if (n == 1 || m == 1) {
      int sum = 0;
      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          sum += grid[i][j];
        }
      }
      return sum;
    }
    for (int i = m - 2; i >= 0; i--) grid[i][n - 1] += grid[i + 1][n - 1];

    for (int j = n - 2; j >= 0; j--) grid[m - 1][j] += grid[m - 1][j + 1];

    for (int i = m - 2; i >= 0; i--) {
      for (int j = n - 2; j >= 0; j--) {
        grid[i][j] += min(grid[i][j + 1], grid[i + 1][j]);
      }
    }
    return grid[0][0];
  }
}
