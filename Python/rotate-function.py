class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        
        len_nums=len(nums)

        def func_k(k:int)->int:
            func_result=0
            for i in range(len_nums):
                func_result+=i*nums[(i+k)%len_nums]
            return func_result
        result=func_k(0)
        f=result
        sum_nums=sum(nums)
        for k in range(len_nums-1):
            f=f+sum_nums-len_nums*nums[-k-1]
            result= max(result,f)

        return result


def run_tests():
    sol = Solution()

    tests = [
        ([4, 3, 2, 6], 26),
        ([100], 0),
        ([1, 2], 2),
        ([0, 0, 0], 0),
        ([-1, -2, -3], -5),
        ([1, 2, 3], 8),
    ]

    for i, (nums, expected) in enumerate(tests, start=1):
        result = sol.maxRotateFunction(nums)

        print(f"Test {i}: {nums}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()