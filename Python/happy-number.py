class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set({1})
        while n not in seen:
            seen.add(n)
            n = sum([int(num) ** 2 for num in str(n)])
        return n == 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(19))  # True
    print(solution.isHappy(2))  # False
