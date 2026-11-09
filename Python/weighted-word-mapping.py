class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        return "".join(chr(ord('z')-(sum(weights[ord(c)-ord('a')] for c in word)%26)) for word in words)






def run_tests():
    sol = Solution()

    tests = [
        (
            ["abcd", "def", "xyz"],
            [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2],
            "rij",
        ),
        (
            ["a", "b", "c"],
            [1] * 26,
            "yyy",
        ),
        (
            ["abcd"],
            [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5],
            "g",
        ),
        (
            ["z"],
            [1] * 25 + [26],
            "z",
        ),
        (
            ["abc"],
            [26] * 26,
            "z",
        ),
    ]

    failed = 0

    for i, (words, weights, expected) in enumerate(tests, start=1):
        result = sol.mapWordWeights(words, weights)

        print(f"Test {i}")
        print(f"words:    {words}")
        print(f"weights:  {weights}")
        print(f"result:   {result!r}")
        print(f"expected: {expected!r}")

        if result == expected:
            print("Passed\n")
        else:
            print("FAILED\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()