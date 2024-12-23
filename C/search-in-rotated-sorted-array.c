#include <stdio.h>


int search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;
    
    while (left <= right) {
        int isAssending=nums[left]<nums[right];
        int mid = left + (right - left) / 2; 
        
        if (nums[mid] == target) {
            return mid; 
        } else if (nums[mid] < target) {
            left = mid + 1; 
        } else {
            right = mid - 1; 
        }
    }
    
    return -1; // Target not found
}


int main() {
    int nums[] = {1,3,5};
    int target = 3;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int result = search(nums, numsSize, target);
    printf("Index of target %d is: %d\n", target, result);
    return 0;
}
