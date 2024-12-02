class Solution {
  double findMedianSortedArrays(List<int> nums1, List<int> nums2) {
    int start1 = 0, start2 = 0;
    int end1 = nums1.length, end2 = nums2.length;
    double median(List<int> A) => ((A.length % 2 == 1)
            ? A[A.length ~/ 2]
            : ((A[A.length ~/ 2 - 1] + A[A.length ~/ 2]) / 2))
        .toDouble();

    return 2.0;
  }
}
void main() {
  List<int> nums1 = [1, 2,3];
  List<int> nums2 = [3, 4];
  Solution solution = Solution();
  double result = solution.findMedianSortedArrays(nums1, nums2);
  print("The median is: $result");
}