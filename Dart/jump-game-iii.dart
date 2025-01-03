class Solution {
  bool canReach(List<int> arr, int start) {
    int length = arr.length;
    List<bool> visited = List.filled(length, false);
    List<int> stack = [start];
    while (stack.isNotEmpty) {
      int index = stack.removeLast();
      visited[index] = true;
      int val = arr[index];
      if (val == 0) return true;
      if (index + val < length && !visited[index + val])stack.add(index + val); 
      if (0 <= index - val && !visited[index - val])stack.add(index - val);
    }
    return false;
  }
}
