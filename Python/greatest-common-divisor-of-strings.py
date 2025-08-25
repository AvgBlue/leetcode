class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisible(dividend: str, divisor: str):
            len_divisor = len(divisor)
            len_dividend = len(dividend)
            remainder = len_dividend % len_dividend
            if remainder != 0:
                return False
            quotient = len_dividend // len_divisor
            return divisor * quotient == dividend

        if str1 == str2:
            return str1
        max_divisor = ""
        i = 1
        while str1[0:i] == str2[0:i]:
            if is_divisible(str1, str1[0:i]) and is_divisible(str2, str1[0:i]):
                max_divisor = str1[0:i]
            i += 1

        return max_divisor


if __name__ == "__main__":
    str1 = "ABCABCABC"
    str2 = "ABCABC"
    sol = Solution()
    result = sol.gcdOfStrings(str1, str2)
    print("GCD of strings:", result)
