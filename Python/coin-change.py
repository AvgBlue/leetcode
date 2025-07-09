from typing import Dict, List, Tuple
from typing import Optional
import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        len_coins = len(coins)
        dp: Dict[Tuple[int, int], int] = {
            **{(len_coins, i): -1 for i in range(-1, amount + 1)},
            **{(j, -1): -1 for j in range(0, len_coins + 1)},
            **{(j, 0): 0 for j in range(0, len_coins)},
        }  # (index, amount)
        for i in range(1, amount + 1):  # amount
            for j in range(len_coins - 1, -1, -1):  # index
                skip = dp[(j + 1, i)]
                take = dp[j, max(-1, i - coins[j])]
                take += 1 if take != -1 else 0
                result = 0
                if take != -1 and skip != -1:
                    result = min(take, skip)
                elif take != -1:
                    result = take
                elif skip != -1:
                    result = skip
                else:
                    result = -1
                dp[(j, i)] = result
        return dp[(0, amount)]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    sol = Solution()
    print(sol.coinChange(coins, amount))
