class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        len_prices=len(prices)

        max_prices_from_i=[prices[-1]]*len_prices
        for i in range(len_prices-2,-1,-1):
            num=prices[i]
            max_prices_from_i[i]=max(max_prices_from_i[i+1],num)

        min_prices=prices[0]
        result=0
        for i in range(1,len_prices):
            num=prices[i]
            min_prices=min(min_prices,num)
            result=max(max_prices_from_i[i]-min_prices,result)
        return result
        
        


def run_tests():
    sol = Solution()

    tests = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([5], 0),
        ([1, 2, 3, 4, 5], 4),
        ([3, 2, 6, 1, 4], 4),
        ([2, 4, 1], 2),
        ([2, 1, 2, 1, 0, 1, 2], 2),
    ]

    failed = 0

    for i, (prices, expected) in enumerate(tests, start=1):
        result = sol.maxProfit(prices)

        print(f"Test {i}: {prices}")
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