import heapq
from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int] ) -> list[int]:
            server_request_count=[0]*k

            min_heap=[]

            available=SortedList(range(k))

            for i,(time,duration) in enumerate(zip(arrival,load)):

                while min_heap and min_heap[0][0]<=time:
                    _,server=heapq.heappop(min_heap)
                    available.add(server)
                if not available:
                    continue

                index=available.bisect_left(i%k)
                if index==len(available):
                    index=0
                server=available.pop(index)
                server_request_count[server]+=1
                heapq.heappush(min_heap,(time+duration,server))

            result=[]
            max_load=max(server_request_count)
            for i,time in enumerate(server_request_count):
                if time==max_load:
                    result.append(i)
            return result



def run_tests():
    sol = Solution()

    tests = [
        (
            3,
            [1, 2, 3, 4, 5],
            [5, 2, 3, 3, 3],
            [1],
        ),
        (
            3,
            [1, 2, 3, 4],
            [1, 2, 1, 2],
            [0],
        ),
        (
            3,
            [1, 2, 3],
            [10, 12, 11],
            [0, 1, 2],
        ),
        (
            1,
            [1, 2, 3],
            [1, 1, 1],
            [0],
        ),
        (
            2,
            [1, 2, 3, 4],
            [10, 10, 10, 10],
            [0, 1],
        ),
    ]

    failed = 0

    for i, (k, arrival, load, expected) in enumerate(tests, start=1):
        result = sol.busiestServers(k, arrival[:], load[:])

        print(f"Test {i}")
        print(f"k:        {k}")
        print(f"arrival:  {arrival}")
        print(f"load:     {load}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        if sorted(result) == sorted(expected):
            print("Passed\n")
        else:
            print("FAILED\n")
            failed += 1

    print(f"{len(tests) - failed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()