#include <stdio.h>
#include <stdlib.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    char* prefix=(char*)calloc(1,200);
    if(strsSize==1){
        return strs[0];
    }
    for(int i=0;strs[i]!='\0'&&i<200;i++){
        char c = strs[0][i];
        for(int j=1;i<strsSize;j++){
            if('\0'==strs[j][i]||c!=strs[j][i]){
                return prefix;
            }
        }
        prefix[i]=c;
    }
    return prefix;
}
int main() {
    char* strs[] = {"flower", "flow", "flight"};
    int strsSize = 3;
    char* result = longestCommonPrefix(strs, strsSize);
    printf("Longest Common Prefix: %s\n", result);
    free(result);
    return 0;
}