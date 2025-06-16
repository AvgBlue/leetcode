from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    obj = NumArray(nums)
    print(obj.sumRange(1, 3))  # Output: 9 (2+3+4)
    print(obj.sumRange(0, 4))  # Output: 15 (1+2+3+4+5)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
