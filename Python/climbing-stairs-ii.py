class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        INF = float("inf")

        acc_costs = [0, INF, INF, INF]
        result = 0

        for i in range(n + 1):
            current_cost = acc_costs[0]

            for step in range(1, 4):
                j = i + step

                if j > n:
                    break

                travel_cost = step ** 2 + costs[j - 1]

                acc_costs[step] = min(
                    acc_costs[step],
                    current_cost + travel_cost
                )

            result = current_cost

            acc_costs[0], acc_costs[1], acc_costs[2], acc_costs[3] = (
                acc_costs[1],
                acc_costs[2],
                acc_costs[3],
                INF
            )

        return result
        



def run_tests():
    sol = Solution()

    tests = [
        # (
        #     4,
        #     [1, 2, 3, 4],
        #     13,
        # ),
        # (
        #     1,
        #     [5],
        #     6,
        # ),
        # (
        #     2,
        #     [5, 1],
        #     5,
        # ),
        # (
        #     3,
        #     [1, 100, 1],
        #     7,
        # ),
        # (
        #     5,
        #     [1, 1, 1, 1, 1],
        #     10,
        # ),
        (
            120,
            [
                655, 115, 26, 760, 282, 251, 229, 143, 755, 105,
                693, 759, 914, 559, 90, 605, 433, 33, 31, 96,
                224, 239, 518, 617, 28, 575, 204, 734, 666, 719,
                559, 430, 226, 460, 604, 285, 829, 891, 7, 778,
                826, 164, 715, 433, 349, 285, 160, 221, 981, 782,
                345, 105, 95, 390, 100, 368, 868, 353, 619, 271,
                827, 45, 748, 471, 550, 128, 997, 945, 388, 81,
                566, 301, 850, 644, 634, 907, 883, 371, 592, 197,
                722, 72, 47, 678, 234, 792, 297, 82, 876, 239,
                888, 104, 390, 285, 465, 651, 855, 374, 167, 380,
                364, 215, 687, 274, 719, 960, 700, 664, 74, 624,
                651, 176, 547, 747, 251, 168, 474, 389, 277, 948
            ],
            12626,
        ),
    ]

    failed = 0

    for i, (n, costs, expected) in enumerate(tests, start=1):
        result = sol.climbStairs(n, costs[:])

        print(f"Test {i}")
        print(f"n:        {n}")
        print(f"costs:    {costs}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        if result == expected:
            print("Passed\n")
        else:
            print("FAILED\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
