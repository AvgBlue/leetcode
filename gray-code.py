import random
from typing import List
from typing import Optional


class Solution:
    def grayCode(self, n: int) -> List[int]:
        list: List[int] = [0]
        for i in range(1, n + 1):
            list.append(list[i - 1] + 2 ** (i - 1))
        return Solution.backtrack(n, list)

    @staticmethod
    def backtrack(n: int, list: List[int]) -> Optional[List[int]]:
        if len(list) == 2**n:
            for i in range(n):
                if list[-1] == 2**i:
                    return list
            return None
        randomList: List[int] = Solution.randomArray(n)
        for i in randomList:
            if Solution.flip_bit(list[-1], i) not in list:
                list.append(Solution.flip_bit(list[-1], i))
                result = Solution.backtrack(n, list)
                if result is None:
                    list.pop()
                else:
                    return result
        return None

    @staticmethod
    def randomArray(n: int) -> List[int]:
        arr: List[int] = [i for i in range(0, n)]  # list(range(0, n))
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    @staticmethod
    def flip_bit(num: int, bit_position: int) -> int:
        return num ^ (1 << bit_position)


if __name__ == "__main__":
    n = 3
    solution = Solution()
    result = solution.grayCode(n)
    print("Gray Code sequence:", result)
