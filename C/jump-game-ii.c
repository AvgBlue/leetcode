int jump(int* nums, int numsSize) {
    if(numsSize==1)return 1;
    int jumps[numsSize];
    for(int i=0;i<numsSize;i++){
        jumps[nums]
    }
    int minJump=numsSize-1;
    for(int i=2;i<=numsSize;i++){
        if(numsSize-i+nums[numsSize-i]>=minJump){
            minJump=numsSize-i;
        }
    }
    return minJump==0;
}