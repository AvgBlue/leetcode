class Solution:
    def combinationSum(
        self,
        candidates: list[int],
        target: int
    ) -> list[list[int]]:

        len_cands = len(candidates)
        vec = [0] * len_cands
        vector_results = []

        def loop(i: int, current_sum: int):
            if current_sum == target:
                vector_results.append(vec[:])
                return

            if i >= len_cands:
                return

            cand = candidates[i]

            max_amount = (target - current_sum) // cand

            for amount in range(max_amount + 1):
                vec[i] = amount

                new_sum = current_sum + amount * cand

                loop(i + 1, new_sum)

            vec[i] = 0

        loop(0, 0)

        result = []

        for vec in vector_results:
            combination = []

            for cand, amount in zip(candidates, vec):
                combination += [cand] * amount

            result.append(combination)

        return result


def run_tests():
    sol = Solution()

    tests = [
        (
            [2, 3, 6, 7],
            7,
            [[2, 2, 3], [7]],
        ),
        (
            [2, 3, 5],
            8,
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        ),
        (
            [2],
            1,
            [],
        ),
        (
            [1],
            2,
            [[1, 1]],
        ),
        (
            [2, 4],
            6,
            [[2, 2, 2], [2, 4]],
        ),
    ]

    failed = 0

    for i, (candidates, target, expected) in enumerate(tests, start=1):
        result = sol.combinationSum(candidates, target)

        # Sort inside each combination and sort the outer list
        result_normalized = sorted(sorted(x) for x in result)
        expected_normalized = sorted(sorted(x) for x in expected)

        print(f"Test {i}")
        print(f"candidates: {candidates}")
        print(f"target:     {target}")
        print(f"result:     {result}")
        print(f"expected:   {expected}")

        if result_normalized == expected_normalized:
            print("Passed\n")
        else:
            print("FAILED")

            result_set = {tuple(x) for x in result_normalized}
            expected_set = {tuple(x) for x in expected_normalized}

            print(f"missing: {expected_set - result_set}")
            print(f"extra:   {result_set - expected_set}\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
