#include <stdio.h>
#include <stdbool.h>

#define SWAP(a, b) { int temp = a; a = b; b = temp; }

void reverseArray(int* nums, int numSize) {
    int start = 0;
    int end = numSize - 1;
    while (start < end) {
        SWAP(nums[start], nums[end]);
        start++;
        end--;
    }
}

void nextPermutation(int* nums, int numsSize) {
    int pivotIndex = -1;

    for (int i = numsSize - 2; i >= 0; i--) {
        if (nums[i] < nums[i + 1]) {
            pivotIndex = i;
            break;
        }
    }

    if (pivotIndex == -1) {
        reverseArray(nums, numsSize);
        return;
    }

    for (int i = numsSize - 1; i > pivotIndex; i--) {
        if (nums[i] > nums[pivotIndex]) {
            SWAP(nums[pivotIndex], nums[i]);
            break;
        }
    }

    reverseArray(nums + pivotIndex + 1, numsSize - pivotIndex - 1);
}
