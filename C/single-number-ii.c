

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



int singleNumber(int* nums, int numsSize) {
    int array[32]={0};
    for(int i=0;i<numsSize;i++){
        int num=nums[i];
        for(int j=0;j<32;j++){
            array[j]=(array[j]+GET_BIT(num,j))%3;
        }
    }
    unsigned int result=0;
    for(int i=0;i<32;i++){
        if(array[i]==1){
            SET_BIT(result,i);
        }
    }
    return result;
}