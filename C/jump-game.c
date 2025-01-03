bool canJump(int* nums, int numsSize){
    if(numsSize==1)return true;
    if(nums[0]==0)return false;
    int minJump=numsSize-1;
    for(int i=2;i<=numsSize;i++){
        if(numsSize-i+nums[numsSize-i]>=minJump){
            minJump=numsSize-i;
        }
    }
    return minJump==0;
}



