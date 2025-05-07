class Solution {
  String minWindow(String s, String t) {
    int sLen = s.length;
    int tLen = t.length;
    if (sLen < tLen) return "";
    Map<String, int> tCharCount = {};
    for (int i = 0; i < tLen; i++) {
      tCharCount[t[i]] = (tCharCount[t[i]] ?? 0) + 1;
    }
    Map<String, int> sCharCount = {};
    for (int i = 0; i < sLen; i++) {
      sCharCount[s[i]] = (sCharCount[s[i]] ?? 0) + 1;
    }

    for (String key in tCharCount.keys) {
      if (!sCharCount.containsKey(key) || sCharCount[key]! < tCharCount[key]!) {
        return "";
      }
    }

    int start = 0;
    int end = sLen - 1;
    for (int i = 0; i < sLen && start < end; i++) {
      print(tCharCount);
      print(sCharCount);
      print(s.substring(start, end + 1));
      String sStart = s[start];

      if (tCharCount.containsKey(sStart)) {
        if (sCharCount[sStart]! > tCharCount[sStart]!) {
          print("removing ${sStart} at $start");
          start++;
          sCharCount[sStart] = sCharCount[sStart]! - 1;
          continue;
        }
      } else {
        print("removing ${sStart} at $start");
        start++;
        continue;
      }

      String sEnd = s[end];
      if (tCharCount.containsKey(sEnd)) {
        if (sCharCount[sEnd]! > tCharCount[sEnd]!) {
          print("removing ${sEnd} at $end");
          end--;
          sCharCount[sEnd] = sCharCount[sEnd]! - 1;
          continue;
        }
      } else {
        print("removing ${sEnd} at $end");
        end--;
        continue;
      }
    }
    print(start);
    print(end);
    return s.substring(start, end + 1);
  }
}

void main() {
  Solution solution = Solution();
  String s = "ADOBECODEBANC";
  String t = "ABC";
  String result = solution.minWindow(s, t);
  print(result); // Expected output: "BANC"
}
