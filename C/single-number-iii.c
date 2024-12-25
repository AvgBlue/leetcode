

// Macro to get the value of a specific bit in an integer
#define GET_BIT(num, pos) (((num) >> (pos)) & 0b1u)

// Macro to set a specific bit in an integer
#define SET_BIT(num, pos) ((num) |= (0b1u << (pos)))

// Macro to clear a specific bit in an integer
#define CLEAR_BIT(num, pos) ((num) &= ~(0b1u << (pos)))

// Macro to toggle a specific bit in an integer
#define TOGGLE_BIT(num, pos) ((num) ^= (0b1u << (pos)))

// Macro to check if a specific bit is set
#define IS_BIT_SET(num, pos) (((num) & (0b1u << (pos))) != 0b0u)

// Macro to modify a bit to a specific value (0 or 1)
#define MODIFY_BIT(num, pos, value) \
    ((num) = ((num) & ~(0b1u << (pos))) | ((value) << (pos)))


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    if(numsSize==2){
        *returnSize=2;
        return nums;
    }

    int bitMask=0;

    for(int i=0;i<numsSize;i++){
        bitMask^=nums[i];
    }

    int* result =(int*)malloc(sizeof(int)*2);  

    for(int i=0;i<32;i++){
        if(GET_BIT(bitMask,i)==0)continue;
        
        int num=0;
        for(int j=0;j<numsSize;j++){
            if(GET_BIT(nums[j],i)==0)continue;
            num^=nums[j];
        }
        result[0]=num;
        break;
    }
    result[1]=bitMask^result[0];
    *returnSize=2;
    return result;
}