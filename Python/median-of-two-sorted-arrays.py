from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getmedian(arr: List[int]) -> float:
            n = len(arr)
            if n % 2 == 1:
                return float(arr[n // 2])
            else:
                return (arr[n // 2 - 1] + arr[n // 2]) / 2.0

        len_nums1: int = len(nums1)
        len_nums2: int = len(nums2)
        if not len_nums1:
            return getmedian(nums2)
        elif not len_nums2:
            return getmedian(nums1)




if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
