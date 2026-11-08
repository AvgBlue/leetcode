

class Solution:
    gcd_table = gcd_table = [
    [False, True, False, False, False, False, False, False, False, False],
    [True, True, True, True, True, True, True, True, True, True],
    [False, True, False, True, False, True, False, True, False, True],
    [False, True, True, False, True, True, False, True, True, False],
    [False, True, False, True, False, True, False, True, False, True],
    [False, True, True, True, True, False, True, True, True, True],
    [False, True, False, False, False, True, False, True, False, False],
    [False, True, True, True, True, True, True, False, True, True],
    [False, True, False, True, False, True, False, True, False, True],
    [False, True, True, False, True, True, False, True, True, False],
]
    def countBeautifulPairs(self, nums: list[int]) -> int:
            len_nums=len(nums)
            result=0
            first_digit_counter=[0]*10
            for j in range(1,len_nums):
                last_digit=nums[j]%10
                i=j-1
                num = nums[i]
                if num >= 1000:
                    first_digit = num // 1000
                elif num >= 100:
                    first_digit = num // 100
                elif num >= 10:
                    first_digit = num // 10
                else:
                    first_digit = num
                first_digit_counter[first_digit]+=1
                if self.gcd_table[0][last_digit]:
                    result += first_digit_counter[0]
                if self.gcd_table[1][last_digit]:
                    result += first_digit_counter[1]
                if self.gcd_table[2][last_digit]:
                    result += first_digit_counter[2]
                if self.gcd_table[3][last_digit]:
                    result += first_digit_counter[3]
                if self.gcd_table[4][last_digit]:
                    result += first_digit_counter[4]
                if self.gcd_table[5][last_digit]:
                    result += first_digit_counter[5]
                if self.gcd_table[6][last_digit]:
                    result += first_digit_counter[6]
                if self.gcd_table[7][last_digit]:
                    result += first_digit_counter[7]
                if self.gcd_table[8][last_digit]:
                    result += first_digit_counter[8]
                if self.gcd_table[9][last_digit]:
                    result += first_digit_counter[9]
            return result


def run_tests():
    sol = Solution()

    tests = [
        (
            [2, 5, 1, 4],
            5,
        ),
        (
            [11, 21, 12],
            2,
        ),
        (
            [31, 25, 72, 79, 74],
            7,
        ),
    ]

    failed = 0

    for i, (nums, expected) in enumerate(tests, start=1):
        result = sol.countBeautifulPairs(nums)

        print(f"Test {i}")
        print(f"nums:     {nums}")
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