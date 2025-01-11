class Solution {
  String generateTag(String str) {
  List<int> freq = List.filled(26, 0);

  for (int i = 0; i < str.length; i++) {
    int charIndex = str.codeUnitAt(i) - 'a'.codeUnitAt(0);
    freq[charIndex]++;
  }

  StringBuffer buffer = StringBuffer();
  for (int i = 0; i < 26; i++) {
    if (freq[i] > 0) {
      buffer.write(String.fromCharCode('a'.codeUnitAt(0) + i));
      buffer.write(freq[i]);
    }
  }

  return buffer.toString();
}


  List<List<String>> groupAnagrams(List<String> strs) {
  List<List<String>> result = [];
  Map<String, int> indexMap = {};

  for (String str in strs) {
    String key = generateTag(str);
    if (!indexMap.containsKey(key)) {
      indexMap[key] = result.length;
      result.add([]);
    }
    result[indexMap[key]!].add(str);
  }

  return result;
}

}
