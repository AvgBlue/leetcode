class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parenthesis_map={0:[""],1:['()']}
        if n==0 or n==1:
            return parenthesis_map[n]
        for i in range(2,n+1):
            result=set()
            for key in parenthesis_map.keys():
                for paren1 in parenthesis_map[key]:
                    for paren2 in parenthesis_map[i-key-1]:
                        result.add(f"({paren1}){paren2}")
            parenthesis_map[i]=list(result)
        return parenthesis_map[n]








def run_tests():
    sol = Solution()

    tests = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (
            4,
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
        ),
    ]

    for i, (n, expected) in enumerate(tests, start=1):
        result = sol.generateParenthesis(n)

        print(f"Test {i}: n = {n}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        result_set = set(result)
        expected_set = set(expected)

        missing = expected_set - result_set
        extra = result_set - expected_set

        if missing:
            print(f"MISSING: {missing}")

        if extra:
            print(f"EXTRA:   {extra}")

        assert result_set == expected_set

        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()