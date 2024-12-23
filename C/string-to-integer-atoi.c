#include <stdbool.h>
#include <limits.h>
#include <stdint.h>

int charToInt(char c) {
    return c - '0';
}

int clamp_to_int32(long long x) {
    if (x < INT32_MIN) {
        return INT32_MIN;
    } else if (x > INT32_MAX) {
        return INT32_MAX;
    } else {
        return (int)x;
    }
}

int myAtoi(char* s) {
    long long result=0;
    while(s[0]!='\0'&&s[0] ==' ')s++;
    bool isNegaive=false;
    if(s[0]=='-'||s[0]=='+'){
        isNegaive= s[0]=='-';
        s++;
    }
    if(isNegaive){
        for(;'0'<=s[0]&&s[0]<='9';s++){
            result-=charToInt(s[0]);
            if(result < INT32_MIN){
                return INT32_MIN;
            }
            result*=10;
        }
        result/=10;
        return (int)result;
    }
    for(;('0'<=s[0]&&s[0]<='9');s++){
        result+=charToInt(s[0]);
        if(result > INT32_MAX){
            return INT32_MAX;
        }
        result*=10;
    }
    result/=10;
    return (int)result;
}

