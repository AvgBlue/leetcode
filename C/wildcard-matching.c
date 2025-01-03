#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char **charArray;


bool isMatch2(char* s,char* p,int sLen,int pLen){
    if(charArray[sLen][pLen]) return charArray[sLen][pLen]>0;
    if(sLen==0&&pLen==0){
        charArray[sLen][pLen]=1;
        return true;
    } 
    if(pLen==0){
        charArray[sLen][pLen]=-1;
        return false;
    } 
    if(sLen==0){
        bool result= p[0]=='*'&&isMatch2(s,p+1,sLen,pLen-1);
        charArray[sLen][pLen]=(result)?1:-1;
        return result;
    } 
    if(p[0]=='?') {
    bool result = isMatch2(s+1,p+1,sLen-1,pLen-1);
    charArray[sLen][pLen] = (result) ? 1 : -1;
    return result;
    }
    if(p[0]=='*') {
    bool result = isMatch2(s+1,p,sLen-1,pLen) || isMatch2(s,p+1,sLen,pLen-1);
    charArray[sLen][pLen] = (result) ? 1 : -1;
    return result;
    }
    bool result = s[0]==p[0] && isMatch2(s+1,p+1,sLen-1,pLen-1);
    charArray[sLen][pLen] = (result) ? 1 : -1;
    return result;
}

bool isMatch(char* s, char* p) {
    int sLen = strlen(s);
    int pLen = strlen(p);
    
    charArray = (char **)malloc((sLen + 1) * sizeof(char *));
    for (int i = 0; i <= sLen; i++) {
        charArray[i] = (char *)malloc((pLen + 1) * sizeof(char));
        memset(charArray[i], 0, (pLen + 1) * sizeof(char));
    }

    bool result=isMatch2(s,p,sLen,pLen); 



    for (int i = 0; i <= sLen; i++) {
        free(charArray[i]);
    }
    free(charArray);
    return result;
}

// Test helper
void test(char *s, char *p, bool expected, int testCase) {

    bool result = isMatch(s, p);
    if (result == expected) {
        printf("Test Case %d: PASS\n", testCase);
    } else {
        printf("Test Case %d: FAIL (Input: \"%s\", Pattern: \"%s\", Expected: %s, Got: %s)\n",
               testCase, s, p, expected ? "true" : "false", result ? "true" : "false");
    }
}



int main() {
    // Test cases
    test("aa", "a", false, 1);
    test("aa", "*", true, 2);
    test("cb", "?a", false, 3);
    test("adceb", "*a*b", true, 4);
    test("acdcb", "a*c?b", false, 5);
    test("", "*", true, 6);
    test("abc", "a*b*c", true, 7);
    test("abc", "a*b*d", false, 9);
    test("xyz", "x?*", true, 10);

    return 0;
}