class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if(num*9<sum):
            return ""
        result=""
        result="9"*(sum//9)
        if len(result)<num:
            result+=str(sum%9)
        if len(result)<num:
            result+="0"*(num-len(result))

        return result
                


def run_tests():
    sol = Solution()

    tests = [
        (2, 3, "30"),
        (2, 17, "98"),
        (1, 10, ""),
        (1, 9, "9"),
        (3, 18, "990"),
        (3, 1, "100"),
        (4, 36, "9999"),
        (4, 35, "9998"),
        (5, 5, "50000"),
        (2, 20, ""),
    ]

    for i, (num, target_sum, expected) in enumerate(tests, start=1):
        result = sol.maxSumOfSquares(num, target_sum)

        print(f"Test {i}")
        print(f"num:      {num}")
        print(f"sum:      {target_sum}")
        print(f"result:   {result!r}")
        print(f"expected: {expected!r}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()