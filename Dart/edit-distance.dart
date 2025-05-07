import 'dart:math';

class Solution {
  int minDistance(String word1, String word2) {
    if (word1 == word2) {
      return 0;
    }
    if (word1.length == word2.length) {
      if (word1[0] == word2[0]) {
        return minDistance(word1.substring(1), word2.substring(1));
      }
      return 1 +
          minDistance("${word2[0]}${word1.substring(1)}", word2.substring(1));
    }
    



    return 1;
  }
}
