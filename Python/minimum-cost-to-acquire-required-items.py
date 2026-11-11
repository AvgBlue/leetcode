class Solution:
    def minimumCost1(
        self,
        cost1: int,
        cost2: int,
        costBoth: int,
        need1: int,
        need2: int
    ) -> int:

        INF = float("inf")
        result = INF

        m = need2 - need1

        if costBoth < cost1:

            if m >= 0:
                y = m if cost2 < costBoth else 0

                result1 = cost2 * y + (need2 - y) * costBoth

                y = m
                result2 = cost2 * y + need1 * costBoth

                result = min(result1,result2)
            else:
                y = 0 
                result = need1 * costBoth

        else:

            if m >= 0:

                y = m if cost2 < costBoth else 0
                result1 = cost2 * y + (need2 - y) * costBoth

                slope = cost1 + cost2 - costBoth
                y = need2 if slope < 0 else m
                x = need1 - need2 + y
                result2 = (cost1 * x+ cost2 * y+ (need2 - y) * costBoth)

                result = min(result1, result2)

            else:
                slope = cost1 + cost2 - costBoth
                y= need2 if slope < 0 else 0
                x = need1 - need2 + y

                result = (cost1 * x+ cost2 * y+ (need2 - y) * costBoth)

        return result

    def minimumCost(
    self,
    cost1: int,
    cost2: int,
    costBoth: int,
    need1: int,
    need2: int
) -> int:

        z1 = 0
        z2 = min(need1, need2)
        z3 = max(need1, need2)

        cost_z1 = (
            cost1 * need1
            + cost2 * need2
        )

        cost_z2 = (
            cost1 * max(need1 - z2, 0)
            + cost2 * max(need2 - z2, 0)
            + costBoth * z2
        )

        cost_z3 = costBoth * z3

        return min(cost_z1, cost_z2, cost_z3)


"""
minimize:
    cost1*x + cost2*y + costBoth*z

subject to:
    x + z ≥ need1
    y + z ≥ need2

    x ≥ 0
    y ≥ 0
    z ≥ 0

    x, y, z are integers
"""
        


def run_tests():
    sol = Solution()

    tests = [
        (
            3, 2, 1, 3, 2,
            3,
        ),
        (
            5, 4, 15, 2, 3,
            22,
        ),
        (
            5, 4, 15, 0, 0,
            0,
        ),
        (
            10, 10, 5, 1, 1,
            5,
        ),
        (
            2, 100, 3, 5, 1,
            11,
        ),
        (
            100, 2, 3, 1, 5,
            11,
        ),
        (
            4, 7, 10, 3, 3,
            30,
        ),
        (
            254, 898, 448, 4888, 2137,
            1656130,
        ),
    ]

    failed = 0

    for i, (
        cost1,
        cost2,
        costBoth,
        need1,
        need2,
        expected
    ) in enumerate(tests, start=1):

        result = sol.minimumCost(
            cost1,
            cost2,
            costBoth,
            need1,
            need2
        )

        print(f"Test {i}: "
            f"costs=({cost1}, {cost2}, {costBoth}), "
            f"needs=({need1}, {need2}), "
            f"result={result}, expected={expected}"
        )

        if result == expected:
            print("Passed\n")
        else:
            print("FAILED\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()