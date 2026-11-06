class Solution:
    def findWords(self, words: list[str]) -> list[str]:

        result=[]
        row_list=[2, 3, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3]
        def get_row(c:str):
            c=c.lower()
            return row_list[ord(c)-97]
        for word in words:
            row=get_row(word[0])
            is_valid=True
            for c in word:
                if get_row(c)!=row:
                    is_valid=False
                    break
            if is_valid:
                result.append(word) 
                
        return result


def run_tests():
    sol = Solution()

    tests = [
        (
            ["Hello", "Alaska", "Dad", "Peace"],
            ["Alaska", "Dad"],
        ),
        (
            ["omk"],
            [],
        ),
        (
            ["adsdf", "sfd"],
            ["adsdf", "sfd"],
        ),
        (
            ["A", "S", "D", "F"],
            ["A", "S", "D", "F"],
        ),
        (
            ["typewriter", "qwerty", "row"],
            ["typewriter", "qwerty", "row"],
        ),
    ]

    failed = 0

    for i, (words, expected) in enumerate(tests, start=1):
        result = sol.findWords(words)

        print(f"Test {i}")
        print(f"words:    {words}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        if result == expected:
            print("Passed\n")
        else:
            print("FAILED\n")
            print(f"missing: {set(expected) - set(result)}")
            print(f"extra:   {set(result) - set(expected)}\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()