class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_len = len(s)
        start = 0
        end = s_len - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    print(sol.isPalindrome(s))
