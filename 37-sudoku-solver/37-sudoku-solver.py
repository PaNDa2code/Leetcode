class Solution:
    def isValid(self, board, row, col, num) -> bool:
        
        for x in range(9):
            if board[row][x] == num:
                return False
        
        for y in range(9):
            if board[y][col] == num:
                return False
        
        start_x = (col // 3)*3
        start_y = (row // 3)*3

        for y in range(3):
            for x in range(3):
                if (board[start_y + y][start_x + x] == num):
                    return False
        
        return True

    def findempty(self,board) -> set:

        for y in range(9):
            for x in range(9):
                if board[y][x] == '.':
                    return y , x
        return -1,-1
    
    def solveSudoku(self,board) -> bool:

        y, x = self.findempty(board)

        if y == -1 and x == -1:
            return True
        
        for num in map(str,range(1,10)):

            if self.isValid(board,y,x,num):

                board[y][x] = num

                if self.solveSudoku(board):
                    return True
                
                board[y][x] = '.'

        return False
