class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def funs(s: str) -> int:
            if s in memo.keys():
                return memo[s]
            result = fun(s)
            memo[s] = result
            return result

        def fun(s: str) -> int:
            lens = len(s)
            if lens == 0:
                return 1
            if lens == 1:
                if s[0] == "0":
                    return 0
                return 1
            if s[0] == "0":
                return 0
            if s[0] == "1" or (
                s[0] == "2" and s[1] in ["0", "1", "2", "3", "4", "5", "6"]
            ):
                if s[1] == "0":
                    return funs(s[2:])
                return funs(s[1:]) + funs(s[2:])
            return funs(s[1:])

        return fun(s)


if __name__ == "__main__":
    solution = Solution()
    test_string = "111111111111111111111111111111111111111111111"
    print("Number of ways to decode:", solution.numDecodings(test_string))
