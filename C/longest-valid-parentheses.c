#include <string.h>

int longestValidParentheses(char *s) {
    int result = 0;
    int length = strlen(s);

    for (int i = 0; i < length; i++) {
        int max = 0;
        int stack = 0;

        for (int j = i; j < length; j++) {
            if (s[j] == '(') {
                stack++;
                max++;
                continue;
            }
            
            if (stack == 0) {
                break;
            }

            stack--;
            max++;

            if (stack == 0 && result < max) {
                result = max;
            }
        }

        if (stack > 0) {
            continue;
        }
    }

    return result;
}
