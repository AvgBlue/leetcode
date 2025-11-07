from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_count: dict[str, int] = Counter(magazine)
        for c in ransomNote:
            if c in dict_count and dict_count[c] > 0:
                dict_count[c] -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct("a", "b"))  # False
    print(solution.canConstruct("aa", "ab"))  # False
    print(solution.canConstruct("aa", "aab"))  # True
