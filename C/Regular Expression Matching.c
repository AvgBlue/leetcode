#include <stdbool.h>
#include <string.h>

bool** array;  // Memoization array
bool** visited;  // Visited array to check if subproblem is already solved

// Free memory allocated for 2D arrays
void freeMemory(bool** arr, int rows) {
    for (int i = 0; i < rows; i++) {
        free(arr[i]);
    }
    free(arr);
}

// Helper function to initialize 2D arrays
bool** initializeArray(int rows, int cols) {
    bool** arr = (bool**)malloc(rows * sizeof(bool*));
    for (int i = 0; i < rows; i++) {
        arr[i] = (bool*)malloc(cols * sizeof(bool));
        memset(arr[i], 0, cols * sizeof(bool));  // Initialize to false
    }
    return arr;
}

// Recursive function with memoization
bool isMatch2(char* s, char* p, int s_len, int p_len) {
    if (visited[s_len][p_len]) {  // Check if result is already computed
        return array[s_len][p_len];
    }

    if (s_len == 0 && p_len == 0) return true;  // Both strings fully matched
    if (p_len == 0) return false;  // Pattern exhausted but string not

    bool firstMatch = (s_len > 0) && (s[0] == p[0] || p[0] == '.');

    bool result;
    if (p_len >= 2 && p[1] == '*') {
        // Match zero occurrences or one occurrence
        result = isMatch2(s, p + 2, s_len, p_len - 2) || 
                 (firstMatch && isMatch2(s + 1, p, s_len - 1, p_len));
    } else {
        result = firstMatch && isMatch2(s + 1, p + 1, s_len - 1, p_len - 1);
    }

    visited[s_len][p_len] = true;  // Mark this subproblem as solved
    array[s_len][p_len] = result;  // Store the result
    return result;
}

// Main function
bool isMatch(char* s, char* p) {
    int s_len = strlen(s);
    int p_len = strlen(p);

    // Initialize memoization and visited arrays
    array = initializeArray(s_len + 1, p_len + 1);
    visited = initializeArray(s_len + 1, p_len + 1);

    for(int i = 0; i < s_len;i++){
        for(int j = 0; j < p_len;j++){
            isMatch2(s, p,i,j);
        }
    }
    // Compute the result using the helper function
    bool result = isMatch2(s, p, s_len, p_len);

    // Free allocated memory
    freeMemory(array, s_len + 1);
    freeMemory(visited, s_len + 1);

    return result;
}