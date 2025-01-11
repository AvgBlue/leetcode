class Solution {
  void reverseArray(List<int> array) {
    int start = 0;
    int end = array.length - 1;
    while (start < end) {
      int temp = array[start];
      array[start] = array[end];
      array[end] = temp;
      start++;
      end--;
    }
  }

  void rotate(List<List<int>> matrix) {
    int length = matrix.length;
    for (int i = 0; i < length; i++) {
      for (int j = 0; j < length; j++) {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
      }
    }
    for(int i=0;i<length;i++){
      reverseArray(matrix[i]);
    }
  }
}
