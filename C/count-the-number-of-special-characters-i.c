#include <string.h>

// Macros to handle unsigned int as a bit array
#define SET_BIT(array, index) ((array) |= (1U << (index)))  // Set the bit at 'index' to 1
#define CLEAR_BIT(array, index) ((array) &= ~(1U << (index))) // Clear the bit at 'index'
#define GET_BIT(array, index) (((array) >> (index)) & 1U)   // Get the value of the bit at 'index'
#define TOGGLE_BIT(array, index) ((array) ^= (1U << (index))) // Toggle the bit at 'index'

int numberOfSpecialChars(char* word) {
    int len = strlen(word);
    unsigned int capitle = 0;
    unsigned int lower = 0;
    
    for (int i = 0; i < len; i++) {
        if ('A' <= word[i] && word[i] <= 'Z') {
            SET_BIT(capitle, word[i] - 'A');
            continue;
        }
        if ('a' <= word[i] && word[i] <= 'z') {
            SET_BIT(lower, word[i] - 'a');
        }
    }
    
    int result = 0;
    for (int i = 0; i < 26; i++) {
        if (GET_BIT(capitle, i) && GET_BIT(lower, i)) result++;
    }
    
    return result;
}