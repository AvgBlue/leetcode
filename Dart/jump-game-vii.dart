import 'dart:math';

class Solution {
  bool canReach(String s, int minJump, int maxJump) {
    int length = s.length;
    if (length == 1) return true;
    if (s[length - 1] != '0') return false;
    int maxReach = 0;
    for (int i = 1; i < length; i++) {
      int endjump = min(maxReach + maxJump, length - 1);
      int startjump = minJump + maxReach;
      if (startjump <= i && i <= endjump&&s[i]=='0') {
        maxReach = i;
      }
    }
    return maxReach == length - 1;
  }
}

//i-minJump