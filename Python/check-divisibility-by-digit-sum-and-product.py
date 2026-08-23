from math import prod
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n%(sum(int(c) for c in str(n))+prod(int(c) for c in str(n)))==0


if __name__ == "__main__":
    solution = Solution()

    examples = [
        (99, True),
        (23, False),
    ]

    for n, expected in examples:
        result = solution.checkDivisibility(n)
        print(f"n: {n} | Expected: {expected} | Result: {result}")
