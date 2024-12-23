#include <string.h>

// Macros to handle unsigned int as a bit array
#define SET_BIT(array, index) ((array) |= (1U << (index)))  // Set the bit at 'index' to 1
#define CLEAR_BIT(array, index) ((array) &= ~(1U << (index))) // Clear the bit at 'index'
#define GET_BIT(array, index) (((array) >> (index)) & 1U)   // Get the value of the bit at 'index'
#define TOGGLE_BIT(array, index) ((array) ^= (1U << (index))) // Toggle the bit at 'index'

char* greatestLetter(char* s) {
    int len = strlen(s);
    unsigned int capitle = 0;
    unsigned int lower = 0;
    
    for (int i = 0; i < len; i++) {
        if ('A' <= s[i] && s[i] <= 'Z') {
            SET_BIT(capitle, s[i] - 'A');
            continue;
        }
        if ('a' <= s[i] && s[i] <= 'z') {
            SET_BIT(lower, s[i] - 'a');
        }
    }
    
    int max = 0;
    for (int i = 0; i < 26; i++) {
        if (GET_BIT(capitle, i) && GET_BIT(lower, i)) max=(i>max)?i:max;
    }
    char* result=(char*)malloc(10);
    result[0]='A'+max;
    return result;
}

int main() {
    char s[] = "lEeTcOdE";
    char* result = greatestLetter(s);
    printf("Greatest English letter in upper and lower case: %c\n", result[0]);
    free(result);
    return 0;
}