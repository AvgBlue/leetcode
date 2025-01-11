class Point {
  int x;
  int y;
  Point(this.x, this.y);

  void rotate() {
    int xTemp = x;
    int yTemp = y;
    x = -yTemp;
    y = xTemp;
  }

  void forward(Point vector) {
    x += vector.x;
    y += vector.y;
  }

  void backward(Point vector) {
    x -= vector.x;
    y -= vector.y;
  }

  @override
  String toString() {
    return 'Point(x: $x, y: $y)';
  }
}

class Solution {
  void goBackAndRotate(Point location, Point vector) {
    location.backward(vector);
    vector.rotate();
    location.forward(vector);
  }

  List<int> spiralOrder(List<List<int>> matrix) {
    int n = matrix.length;
    int m = matrix[0].length;
    int size = n * m;

    List<int> result = List.filled(size, 0);

    int top = -1; // row == -1
    int bottom = n; // row == n
    int left = -1; // column == -1
    int right = m; // column == m

    Point location = Point(0, 0);

    Point vector = Point(1, 0);

    for (int i = 0; i < size; i++) {
      print(location);
      result[i] = matrix[location.y][location.x];
      location.forward(vector);
      if (location.y == top) {
        // We just went above row 0
        goBackAndRotate(location, vector);
        left++;
      } else if (location.x == right) {
        // We just went past last column
        goBackAndRotate(location, vector);
        top++;
      } else if (location.y == bottom) {
        // We just went below last row
        goBackAndRotate(location, vector);
        right--;
      } else if (location.x == left) {
        // We just went past column 0
        goBackAndRotate(location, vector);
        bottom--;
      }
    }
    return result;
  }
}

void main() {
  List<List<int>> matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ];

  Solution solution = Solution();
  List<int> result = solution.spiralOrder(matrix);
  print(result);
}
