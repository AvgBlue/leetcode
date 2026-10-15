class Solution:

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
            len_temperatures=len(temperatures)
            answer = [0] * len_temperatures
            for i in range(len_temperatures-2,-1,-1):
                temp1=temperatures[i]
                ans=0
                j=i+1
                while j<len_temperatures:
                    temp2=temperatures[j]
                    if temp2>temp1:
                        ans=j-i
                        break
                    elif answer[j]==0:
                        break
                    else:
                        j+=answer[j]
                answer[i]=ans

                
            return answer
            




def run_tests():
    sol = Solution()

    tests = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),
        ([70], [0]),
        ([70, 70, 70], [0, 0, 0]),
        ([70, 71, 70, 72], [1, 2, 1, 0]),
    ]

    for i, (temperatures, expected) in enumerate(tests, start=1):
        result = sol.dailyTemperatures(temperatures)

        print(f"Test {i}: {temperatures}")
        print(f"result:   {result}")
        print(f"expected: {expected}")

        assert result == expected
        print("Passed\n")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()