#include <limits.h>
double myPow(double x, int n) {
    //base cases for all
    if(n==0)return 1;
    if(x==1) return x;
    if(x==-1) return (n%2)?-1:1;
    if(n<0) return (n!=INT_MIN)?1/myPow(x, -n):1/myPow(x, INT_MAX);
    if(n%2)return x*myPow(x,n-1);
    double result=x;
    while(n%2==0){
        result*=result;
        n>>=1;
    }
    return result*x;
}