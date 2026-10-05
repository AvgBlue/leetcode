class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        len_num=len(nums)
        for num in nums:
            index=abs(num)
            if nums[index-1]<0:
                return index
            nums[index-1]*=-1
        return -1



def run_tests():
    s = Solution()

    print("Test 1")
    nums = [1, 3, 4, 2, 2]
    assert s.findDuplicate(nums) == 2
    print("Passed")

    print("Test 2")
    nums = [3, 1, 3, 4, 2]
    assert s.findDuplicate(nums) == 3
    print("Passed")

    print("Test 3")
    nums = [3, 3, 3, 3, 3]
    assert s.findDuplicate(nums) == 3
    print("Passed")

    print("Test 4")
    nums = [1, 1]
    assert s.findDuplicate(nums) == 1
    print("Passed")

    print("Test 5")
    nums = [1, 4, 6, 3, 2, 5, 6]
    assert s.findDuplicate(nums) == 6
    print("Passed")

    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()