from itertools import combinations
from typing import List, Tuple


class Solution:
    def g(self, subset: Tuple[int, ...], x: int) -> int:
        """Return this subset's intersection-size contribution up to x."""
        raise NotImplementedError

    def inclusion_exclusion(self, coins: List[int], x: int) -> int:
        total = 0

        for subset_size in range(1, len(coins) + 1):
            sign = 1 if subset_size % 2 == 1 else -1

            for subset in combinations(coins, subset_size):
                total += sign * self.g(subset, x)

        return total

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        if 1 in coins:
            return k
        coins.sort()
        prime_coins=[]
        for coin in coins:
            keep=True
            for prime_coin in prime_coins:
                if coin%prime_coin==0:
                    keep =False
                    break
            if keep:
                prime_coins.append(coin)
        low = 1
        high = coins[0] * k

        def count_up_to(x: int) -> int:
            return self.inclusion_exclusion(coins, x)

        while low < high:
            mid = (low + high) // 2

            if count_up_to(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low


if __name__ == "__main__":
    solution = Solution()

    examples = [

        ([6,5],1435065516,0)
    ]

    for coins, k, expected in examples:
        result = solution.findKthSmallest(coins, k)
        print(f"Expected: {expected} | Result: {result}")
