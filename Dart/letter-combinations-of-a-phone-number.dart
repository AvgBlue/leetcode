class Solution {
  List<String> letterCombinations(String digits) {
    if (digits.isEmpty) {
      return [];
    }
    const Map<String, List<String>> digitToLetters = {
      '2': ['a', 'b', 'c'],
      '3': ['d', 'e', 'f'],
      '4': ['g', 'h', 'i'],
      '5': ['j', 'k', 'l'],
      '6': ['m', 'n', 'o'],
      '7': ['p', 'q', 'r', 's'],
      '8': ['t', 'u', 'v'],
      '9': ['w', 'x', 'y', 'z'],
    };
    List<String> result = [''];
    for (String digit in digits.split('')) {
      List<String> newResult = [];
      while (!result.isEmpty) {
        String s = result.removeLast();
        List<String> array = digitToLetters[digit]!;
        int n = array.length;
        for (int i = 0; i < n; i++) {
          newResult.add("${s}${array[i]}");
        }
      }
      result = newResult;
    }
    return result;
  }
}
