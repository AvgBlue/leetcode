from typing import Dict, List, Tuple
import pandas as pd


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len: int = len(s)
        t_len: int = len(t)
        dp: List[int] = [0] * (t_len + 1)
        dp[t_len] = 1

        for i in range(s_len - 1, -1, -1):
            new_dp = dp[:]
            for j in range(t_len - 1, -1, -1):
                new_dp[j] = dp[j] + (dp[j + 1] if s[i] == t[j] else 0)
            dp = new_dp

        return dp[0]

    numDistinct2 = lambda _, s, t: (
        lambda s, t, dp: (
            [
                (
                    dp := [
                        dp[j] + (dp[j + 1] if c == t[j] else 0) for j in range(len(t))
                    ]
                    + [1]
                )
                for c in s[::-1]
            ],
            dp,
        )[1]
    )(s, t, [0] * len(t) + [1])[0]

    def numDistinct6(self, s: str, t: str) -> int:
        return (
            lambda Y: Y(
                lambda f: lambda i, j: (
                    1
                    if j == len(t)
                    else (
                        0
                        if i == len(s)
                        else f(i + 1, j) + (f(i + 1, j + 1) if s[i] == t[j] else 0)
                    )
                )
            )
        )(
            lambda g: (lambda x: g(lambda *a: x(x)(*a)))(
                lambda x: g(lambda *a: x(x)(*a))
            )
        )(
            0, 0
        )


if __name__ == "__main__":
    s = "babgbag"
    t = "bag"
    sol = Solution()
    print(f"\nresult = {sol.numDistinct6(s, t)}")
