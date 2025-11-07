from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter: dict[str, int] = Counter(s)
        t_counter: dict[str, int] = Counter(t)
        return s_counter == t_counter


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))  # Output: True