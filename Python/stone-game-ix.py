import random
from typing import List


class Solution:
    #p1 win so true
    #p2 win so false
    def stoneGameIX(self, stones: List[int]) -> bool:
        counts = [0, 0, 0] # stone%3=0, stone%3=1, stone%3=2
        for stone in stones:
            counts[stone % 3] += 1
        
        sum=0
        result=True
        print(f"counts = {counts}")
        while counts[0]>0 or counts[1]>0 or counts[2]>0:
            took=False
            for i in [0,1,2]:
                if counts[i]>0 and (sum+i)%3!=0:
                    sum=(sum+i)%3
                    counts[i]-=1
                    print(f"{"alice" if result else "bob"} took stone with reminder of {i}")
                    print(f"  new state is {counts} and sum={sum}")
                    took=True
                    break
            if not took:
                print(f"{"alice" if result else "bob"} took stone with reminder of {i} and lose")
                return  not result
            result=not result
        return False


if __name__ == "__main__":
    solution = Solution()

    examples = [
        ([2, 1], True),
        ([2], False),
        ([5, 1, 2, 4, 3], False),
        ([20,3,20,17,2,12,15,17,4],True)
    ]

    for stones, expected in examples:
        result = solution.stoneGameIX(stones)
        print(stones, "->", result, ", expected:", expected)
