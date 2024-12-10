class Solution {
  bool isValid(String s) {
    List<int> stack = [];
    int counterC = 0;
    int counterD = 0;
    int counterB = 0;
    for (String c in s.split('')) {
      if (counterC < 0 || counterD < 0 || counterB < 0) return false;
      if (c == '(') {
        counterC++;
        stack.add(1);
        continue;
      }
      if (c == ')') {
        counterC--;
        if (!stack.isEmpty && stack.last == 1) {
          stack.removeLast();
        } else {
          return false;
        }
        continue;
      }
      if (c == '{') {
        stack.add(2);
        counterD++;
        continue;
      }
      if (c == '}') {
        counterD--;
        if (!stack.isEmpty && stack.last == 2) {
          stack.removeLast();
        } else {
          return false;
        }
        continue;
      }
      if (c == '[') {
        stack.add(3);
        counterB++;
        continue;
      }
      if (c == ']') {
        counterB--;
        if (!stack.isEmpty && stack.last == 3) {
          stack.removeLast();
        } else {
          return false;
        }
        continue;
      }
    }
    return counterC == 0 && counterD == 0 && counterB == 0;
  }
}
