/*

^
[+-]?

(\d+(\.\d*)?   |   (\.\d+))

([eE][+-]?\d+)?

$


*/
#include <stdbool.h>
#include <string.h>
#define IS_DIGIT(c) ((c) >= '0' && (c) <= '9')
#define IS_NOT_DIGIT(c) ((c) < '0' || (c) > '9')


//(\d+(\.\d*)?
int option1(char* s){
    int i=0;
    if(IS_NOT_DIGIT(s[0])){
        return 0;
    }
    while(IS_DIGIT(s[i]))i++;
    if(s[i]!='.'){
        return i;
    }
    i++;
    while(IS_DIGIT(s[i]))i++;
    return i;
}

//(\.\d+))
int option2(char* s){
    if(s[0]!='.'){
        return 0;
    }
    if(IS_NOT_DIGIT(s[1])){
        return 0;
    }
    int i=1;
    while(IS_DIGIT(s[i]))i++;
    return i;
}

int expo(char* s){
    if(s[0]!='E'&&s[0]!='e'){
        return 0;
    }
    int i=1;
    if(s[i]=='+'||s[i]=='-'){
        i++;
    }
    while(IS_DIGIT(s[i]))i++;
    return (strlen(s)==i)?i:0;
}


bool isNumber(char* s) {
    int len=0;
    if(s[0]=='+'||s[0]=='-'){
        len++;
    }
    int len1=option1(s+len);
    int len2=option2(s+len);
    if(len1==0&&len2==0){
        return false;
    }
    if(len1!=0){
        len+=len1;
    }else{
        len+=len2;
    }
    len+=expo(s+len);
    return strlen(s)==len;
}

