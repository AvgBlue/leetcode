class Solution {
  final int BASE = 10;
  List<int> plusOne(List<int> digits) {
    int length = digits.length;
    //check all 9
    bool is9 = true;
    for (int i = 0; is9 && i < length; i++) {
      is9 &= digits[i] == 9;
    }
    if (is9) {
      List<int> result = List.filled(length + 1, 0);
      result[0] = 1;
      return result;
    }
    void fun(int i) {
      if (digits[i] != BASE - 1) {
        digits[i]++;
        return;
      } else {
        digits[i] = 0;
        fun(i - 1);
      }
    }

    fun(length-1);
    return digits;
  }
}
