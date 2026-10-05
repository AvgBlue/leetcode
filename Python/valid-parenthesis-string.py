class Solution:
    def checkValidString(self, s: str) -> bool:
        count=0
        special=0
        for c in s:
            match c:
                case '(':
                    count+=1
                case '*':
                    special+=1
                case ')':
                    if count>0:
                        count-=1
                    elif special>0:
                        special-=1
                    else:
                        return False
        if count>special:
            return False

        count=0
        special=0
        for c in s[::-1]:
            match c:
                case ')':
                    count+=1
                case '*':
                    special+=1
                case '(':
                    if count>0:
                        count-=1
                    elif special>0:
                        special-=1
                    else:
                        return False
        if count>special:
            return False
        return True
                


def run_tests():
    sol = Solution()

    tests = [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
        ("((*)", True),
        ("(((*)", False),
        ("(*()", True),
        (")*(", False),
        ("********", True),
        ("(((((*))))", True),
        ("(((((()*)(*)*))())())(()())())))((**)))))(()())()",False),
        ("(((((*(((((*((**(((*)*((((**))*)*)))))))))((*(((((**(**)",False),
    ]

    for i, (s, expected) in enumerate(tests, start=1):
        result = sol.checkValidString(s)

        print(f"Test {i}: {s!r}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()