class Solution {
  String addBinary(String a, String b) {
    if (a.length < b.length) {
      String temp = a;
      a = b;
      b = temp;
    }
    List<int> aList = List.generate(a.length, (i) {
      if (a[a.length-i-1] == '0')
        return 0;
      else
        return 1;
    });

    void addone(int i) {
      while (true) {
        if (a.length <= i) {
          aList.add(1);
          return;
        } else if (aList[i] == 0) {
          aList[i] = 1;
          return;
        } else {
          aList[i] = 0;
          i++;
        }
      }
    }

    for (int i = 0; i < b.length; i++) {
      if (b[b.length-i-1] == '1') addone(i);
    }

    return List.generate(aList.length, (i) {
      if (aList[i] == 1)
        return '1';
      else
        return '0';
    }).reversed.join('');
  }
}

void main() {
  Solution solution = Solution();
  String a = "1010";
  String b = "1011";
  print(solution.addBinary(a, b)); // Output: "10101"
}
