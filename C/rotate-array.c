void reverseArray(int* nums, int numsSize) {
    int start = 0;
    int end = numsSize - 1;
    while (start < end) {
        // Swap the elements at start and end
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;

        // Move pointers
        start++;
        end--;
    }
}

void rotate(int* nums, int numsSize, int k) {
    reverseArray(nums,numsSize);
    reverseArray(nums,k);
    reverseArray(nums+k,numsSize-k);
}

