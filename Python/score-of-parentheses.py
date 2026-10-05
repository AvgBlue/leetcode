class Unit:
    def val(self)->int:
        return 1


class Uno(Unit):
    def __init__(self,unit:Unit):
        super().__init__()
        self.unit=unit

    def val(self)->int:
        return 2*self.unit.val()

class Duo(Unit):
    def __init__(self,unit1:Unit,unit2:Unit):
            super().__init__()
            self.unit1=unit1
            self.unit2=unit2

    def val(self)->int:
            return self.unit1.val()+self.unit2.val()



class Solution:

    def foldUnit(self, s: str) -> tuple[Unit, str]:
        if s.startswith("()"):
            current = Unit()
            rest = s[2:]
        else:
            inner, rest = self.foldUnit(s[1:])

            current = Uno(inner)
            rest = rest[1:] 


        if not rest or rest[0] == ')':
            return current, rest

        next_unit, rest = self.foldUnit(rest)

        return Duo(current, next_unit), rest

    def scoreOfParentheses(self, s: str) -> int:
        unit=self.foldUnit(s)
        result=unit[0].val()
        

        return result


def run_tests():

    sol = Solution()

    print("Test 1")
    assert sol.scoreOfParentheses("()") == 1
    print("Passed")

    print("Test 2")
    assert sol.scoreOfParentheses("(())") == 2
    print("Passed")

    print("Test 3")
    assert sol.scoreOfParentheses("()()") == 2
    print("Passed")

    print("Test 4")
    assert sol.scoreOfParentheses("(()(()))") == 6
    print("Passed")

    print("Test 5")
    assert sol.scoreOfParentheses("((()))") == 4
    print("Passed")

    print("Test 6")
    assert sol.scoreOfParentheses("(()())") == 4
    print("Passed")

    print("Test 7")
    assert sol.scoreOfParentheses("()(())") == 3
    print("Passed")

    print("Test 8")
    assert sol.scoreOfParentheses("(())()") == 3
    print("Passed")

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()