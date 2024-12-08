class Solution {
  bool isPalindrome(int x) {
    if (x < 0) return false;
    String s = x.toString();
    int n =s.length;
    for (int i = 0; i < n / 2; i++) {
      if(s[i]!=s[n-i-1]){
        return false;
      }
    }
    return true;
  }
}
