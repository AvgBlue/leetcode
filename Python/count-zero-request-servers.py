

class Solution:
    def countServers(self, n: int,logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        len_queries=len(queries)
        len_logs=len(logs)
        logs.sort(key=lambda a : a[1]) 
        queries_indexes = list(range(len_queries))
        queries_indexes.sort(key= lambda i:queries[i])

        server_count=0
        server_count_map=[0]*(n+1)

        start=0
        end =0
        result=[n]*len_queries

        for j in range(len_queries):
            query_index = queries_indexes[j]
            query = queries[query_index]  

            while end<len_logs and logs[end][1]<=query:
                server_id = logs[end][0]
                if server_count_map[server_id] == 0:
                    server_count += 1
                server_count_map[server_id] += 1
                end += 1
            start_val=query-x
            
            while start<len_logs and logs[start][1]<start_val:
                server_id=logs[start][0]
                if server_count_map[server_id]==1:
                    server_count-=1
                server_count_map[server_id]-=1
                start+=1
            
            result[query_index]-=server_count
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
        (
            6,
            [[1,21]],
            10,
            [24,35,28,26,20,25,16,31,12],
            [5,6,5,5,6,5,6,5,6],
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