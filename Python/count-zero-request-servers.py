class Solution:
    def countServers(self, n: int,logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        len_queries=len(queries)
        len_logs=len(logs)
        logs.sort(key=lambda x : x[1]) #[[1, 3], [1, 5],[2, 6]],
        queries.sort() # [10,11]
        





        return []


    def countServers2(self, n: int,logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
            len_queries=len(queries)
            result=[0]*len_queries
            for i,end in enumerate(queries):
                is_received=[False]*n
                for log in logs:
                    index_id=log[0]-1
                    if end-x<=log[1] and log[1]<=end:
                        is_received[index_id]=True
                result[i]=sum((0 if x else 1) for x in is_received)
            return result


def run_tests():
    sol = Solution()

    tests = [
        (
            3,
            [[1, 3], [2, 6], [1, 5]],
            5,
            [10, 11],
            [1, 2],
        ),
        (
            3,
            [[2, 4], [2, 1], [1, 2], [3, 1]],
            2,
            [3, 4],
            [0, 1],
        ),
        (
            2,
            [[1, 1], [2, 2]],
            1,
            [5],
            [2],
        ),
        (
            3,
            [[1, 1], [2, 2], [3, 3]],
            2,
            [3],
            [0],
        ),
        (
            1,
            [[1, 5]],
            3,
            [8, 9],
            [0, 1],
        ),
    ]

    failed = 0

    for i, (n, logs, x, queries, expected) in enumerate(tests, start=1):
        # Copy because your solution may sort/mutate logs
        test_logs = [log[:] for log in logs]
        test_queries = queries[:]

        result = sol.countServers(n, test_logs, x, test_queries)

        print(f"Test {i}")
        print(f"n:        {n}")
        print(f"logs:     {logs}")
        print(f"x:        {x}")
        print(f"queries:  {queries}")
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