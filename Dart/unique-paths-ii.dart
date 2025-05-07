class Solution {
  int uniquePathsWithObstacles(List<List<int>> obstacleGrid) {
    if (obstacleGrid.last.last == 1) return 0;
    int m = obstacleGrid.length;
    int n = obstacleGrid[0].length;
    List<List<int>> memo = List.generate(m, (_) => List.filled(n, -1));    

    int fun(int i, int j) {
      if (memo[i][j] != -1) return memo[i][j];
      if (obstacleGrid[i][j] == 1) return 0;
      if (i == m - 1 && j == n - 1) return 1;
      if (i == m - 1) return fun(i, j + 1);
      if (j == n - 1) return fun(i + 1, j);
      return memo[i][j]=fun(i + 1, j) + fun(i, j + 1);
    }

    return fun(0, 0);
  }
}
