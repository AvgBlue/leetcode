#define GET_BIT(num, index) (((num) >> (index)) & 1)                          // Get the bit at the specified index
#define SET_BIT(num, index) ((num) |= ((__int128)1 << (index)))               // Set the bit at the specified index to 1
#define CLEAR_BIT(num, index) ((num) &= ~((__int128)1 << (index)))            // Clear the bit at the specified index (set to 0)
#define TOGGLE_BIT(num, index) ((num) ^= ((__int128)1 << (index)))            // Toggle the bit at the specified index

bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    __int128 rows = 0;
    __int128 columns = 0;
    __int128 boxs = 0;
    
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') continue;
            int num = board[i][j] - '1';
            if (GET_BIT(rows, 9 * i + num)
                || GET_BIT(columns, 9 * j + num)
                || GET_BIT(boxs, 27 * (i / 3) + 9 * (j / 3) + num)) {
                return false;
            }
            SET_BIT(rows, 9 * i + num);
            SET_BIT(columns, 9 * j + num);
            SET_BIT(boxs, 27 * (i / 3) + 9 * (j / 3) + num);
        }
    }
    return true;
}
char** copyBoard(char** board, int boardSize, int* boardColSize) {
    char** newBoard = (char**)malloc(boardSize * sizeof(char*));
    for (int i = 0; i < boardSize; i++) {
        newBoard[i] = (char*)malloc(boardColSize[i] * sizeof(char));
        for (int j = 0; j < boardColSize[i]; j++) {
            newBoard[i][j] = board[i][j];
        }
    }
    return newBoard;
}


void solveSudoku(char** board, int boardSize, int* boardColSize) {
    char** board1=board;
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            if(board1[i][j]!='.')continue;
            for(int r=1;r<=9;i++){
                char** board2=copyBoard(board1, boardSize, boardColSize);
                board2[i][j]
                if(isValidSudoku())
            }
        }
    }
}