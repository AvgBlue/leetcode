from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr_len = len(gas)
        start_index = 0
        total = 0
        starting_sum = 0
        for i in range(arr_len):
            total += gas[i] - cost[i]
            starting_sum += gas[i] - cost[i]
            if starting_sum < 0:
                start_index = i + 1
                starting_sum = 0
        return start_index if total >= 0 else -1


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    sol = Solution()
    result = sol.canCompleteCircuit(gas, cost)
    print(result)
