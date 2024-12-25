class Solution {
  String countAndSay(int n) {
    String result = "1";
    for (int i = 0; i < n; i++) {
      result = RLE(result);
    }
    return result;
  }

  String RLE(String s) {
    String currentChar = s[0];
    int count = 1;
    StringBuffer result = StringBuffer();
    for (int i = 1; i < s.length; i++) {
      if (s[i] != currentChar) {
        result.write('$count');
        result.write('$currentChar');
        currentChar = s[i];
        count = 1;
      } else {
        count++;
      }
    }
    result.write('$count');
    result.write('$currentChar');
    return result.toString();
  }
}

void main() {
  Solution solution = Solution();
  for (int i = 1; i <= 30; i++) {
    String result = solution.countAndSay(i);
    print("${result.length}");
  }
}
