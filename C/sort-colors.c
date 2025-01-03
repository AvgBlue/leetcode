#include <stdio.h>

#define SWAP(a, b) do { int temp = (a); (a) = (b); (b) = temp; } while (0)

void sortColors(int* nums, int numsSize) {
    int left = 0;              
    int right = numsSize - 1;  
    int i = 0; 
    while(i <= right) {
        printf("Current array: ");
        for (int j = 0; j < numsSize; j++) {
            printf("%d ", nums[j]);
        }
        printf("\n");
        switch (nums[i] )
        {
        case 0:
            SWAP(nums[left], nums[i]);
            left++;
        case 1:
            i++;
            break;
        case 2:
            SWAP(nums[right], nums[i]);
            right--;
            break;
        default:
            break;
        }
    }
    printf("Current array: ");
        for (int j = 0; j < numsSize; j++) {
            printf("%d ", nums[j]);
        }
        printf("\n");
}


int main() {
    int nums1[] = {0, 0, 2, 2, 1, 1};
    int numsSize1 = sizeof(nums1) / sizeof(nums1[0]);
    sortColors(nums1, numsSize1);
    printf("Sorted array 1: ");
    for (int i = 0; i < numsSize1; i++) {
        printf("%d ", nums1[i]);
    }
    printf("\n");

    int nums2[] = {2, 0, 1};
    int numsSize2 = sizeof(nums2) / sizeof(nums2[0]);
    sortColors(nums2, numsSize2);
    printf("Sorted array 2: ");
    for (int i = 0; i < numsSize2; i++) {
        printf("%d ", nums2[i]);
    }
    printf("\n");

    return 0;
}