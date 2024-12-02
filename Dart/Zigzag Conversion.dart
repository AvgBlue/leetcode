class Solution {
  String convert(String s, int numRows) {
    if (numRows == 1) return s;

    String res = "";
    int len = s.length;

    for (int r = 0; r < numRows; r++) {
      int increment = 2 * (numRows - 1);
      for (int i = r; i < len; i += increment) {
        print("res += s[${i}] , i=${i}");
        res += s[i];
        if (r > 0 && r < numRows - 1 && i + increment - 2 * r < len) {
          print("res += s[${i + increment - 2 * r}] , i=${i}");
          res += s[i + increment - 2 * r];
        }

      }
    }
    return res;
  }

  String convert2(String s, int numRows) {
    if (numRows == 1) {
      return s;
    }

    List<StringBuffer> rows =
        List.generate(numRows, (_) => StringBuffer(), growable: false);
    int n = numRows - 1;

    for (int i = 0; i < s.length; i++) {
      int row = n - (i % (2 * n) - n).abs();
      rows[row].write(s[i]);
    }

    StringBuffer result = StringBuffer();
    for (var row in rows) {
      result.write(row);
    }

    return result.toString();
  }
}

void main() {
  Solution solution = Solution();
  String result = solution.convert("123456789", 4);
  print(result);
}
