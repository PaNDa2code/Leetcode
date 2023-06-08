int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int x, y;  // Declare variables here
    
    int neg = 0;
    for (x = 0; x < gridSize; x++) {  // Iterate over the rows using gridSize
        for (y = 0; y < gridColSize[x]; y++) {  // Iterate over the columns in each row
            if (grid[x][y] < 0) {
                neg++;
            }
        }
    }
    return neg;
}
