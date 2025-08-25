from typing import List, Optional


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)

        def find_magic_num(nums) -> int:
            megic_num = -(10**5)
            while megic_num in nums:
                megic_num += 1
            return megic_num

        def mark_all(nums: List[int], magic_num) -> int:
            last_seen_num: Optional[int] = None
            seen_again: bool = False
            count = 0
            for i, num in enumerate(nums):
                if last_seen_num != num:
                    last_seen_num = num
                    seen_again = False
                    continue
                if not seen_again:
                    seen_again = True
                    continue
                nums[i] = magic_num
                count += 1
            return count

        def remove_mark(nums: List[int], magic_num: int):
            write = 0
            for num in nums:
                if num != magic_num:
                    nums[write] = num
                    write += 1

        magic_num = find_magic_num(nums)
        count = mark_all(nums, magic_num)
        remove_mark(nums, magic_num)
        return len_nums - count


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1, 1, 2, 2, 3]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print("Length after removing duplicates:", k)
    print("Modified array:", nums[0:k])
