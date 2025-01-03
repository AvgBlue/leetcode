int trap(int* height, int heightSize) {
    int result=0;
    for(int i=0;i<heightSize;i++){
        int amountStarti=0;
        for(int j=i+1;j<heightSize;j++){
            if(height[i]>height[j]){
                amountStarti+=height[i]-height[j];
            }
            else{
                result+=amountStarti;
                i=j-1;
                break;
            }
        }
    }
    return result;
}