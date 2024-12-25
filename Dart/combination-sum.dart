class Solution {
  List<List<int>> combinationSum(List<int> candidates, int target) {
    List<List<int>> result = [];
    List<int> currentCombination = List.filled(candidates.length, 0);

    void addResult() {
      List<int> combination = [];
      for (int i = 0; i < currentCombination.length; i++) {
        combination.addAll(List.filled(currentCombination[i], candidates[i]));
      }
      result.add(combination);
    }

    int combineSum(List<int> array) {
      int sum = 0;
      for (int i = 0; i < array.length; i++) {
        sum += candidates[i] * array[i];
      }
      return sum;
    }

    void add1(int index) {
      if (index >= currentCombination.length) {
        return;
      }
      currentCombination[index]++;
      if (combineSum(currentCombination) > target) {
        currentCombination[index] = 0;
        add1(index + 1);
      }
    }

    bool keepGoing = true;
    while (keepGoing) {
      if (combineSum(currentCombination) == target) {
        addResult();
      }
      add1(0);
      if (currentCombination.every((x) => x == 0)) {
        keepGoing = false;
      }
    }

    return result;
  }
}
