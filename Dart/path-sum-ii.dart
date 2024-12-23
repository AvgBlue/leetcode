/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

class Solution {
  List<List<int>> pathSum(TreeNode? root, int targetSum) {
    List<List<int>> result = help(root, targetSum);

    void reverseInPlace(List<int> list) {
      int left = 0;
      int right = list.length - 1;
      while (left < right) {
        int temp = list[left];
        list[left] = list[right];
        list[right] = temp;
        left++;
        right--;
      }
    }

    for (List<int> path in result) {
      reverseInPlace(path);
    }
    return result;
  }

  List<List<int>> help(TreeNode? root, int targetSum) {
    if (null == root) {
      return [];
    }
    if (root.left == null && root.right == null && targetSum == root.val) {
      return [
        [targetSum]
      ];
    }

    List<List<int>> childsPath = [];
    for (TreeNode? n in [root.right, root.left]) {
      if (n == null) continue;
      List<List<int>> paths = help(n, targetSum - root.val);
      if (paths.isNotEmpty) {
        childsPath.addAll(paths);
      }
    }
    List<List<int>> result = [];
    for (List<int> l in childsPath) {
      l.add(root.val);
      result.add(l);
    }
    return result;
  }
}

void main() {
  TreeNode root = TreeNode(5);
  root.left = TreeNode(4);
  root.right = TreeNode(8);
  root.left!.left = TreeNode(11);
  root.left!.left!.left = TreeNode(7);
  root.left!.left!.right = TreeNode(2);
  root.right!.left = TreeNode(13);
  root.right!.right = TreeNode(4);
  root.right!.right!.left = TreeNode(5);
  root.right!.right!.right = TreeNode(1);

  Solution solution = Solution();
  int targetSum = 22;
  List<List<int>> result = solution.pathSum(root, targetSum);
  print(result);
}
