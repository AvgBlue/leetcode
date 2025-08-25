class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s)
        i = len_s - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        count = 0
        while i >= 0 and s[i] != " ":
            i -= 1
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    test_str = "Hello World"
    print(sol.lengthOfLastWord(test_str))
