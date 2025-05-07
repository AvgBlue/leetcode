class Solution {
  int lengthOfLastWord(String s) {
    int result = 0;
    int i = s.length - 1;
    while ( 0 <= i&&s[i] == ' ' ) i--;
    while (0 <= i&&s[i] != ' ' ) {
      result++;
      i--;
    }
    return result;
  }
}
