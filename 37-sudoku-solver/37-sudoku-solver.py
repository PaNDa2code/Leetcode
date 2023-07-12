class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num, x, y, board):
            # Check row
            for i in range(9):
                if board[i][x] == num:
                    return False

            # Check column
            for j in range(9):
                if board[y][j] == num:
                    return False

            # Check 3x3 box
            startRow = (y // 3) * 3
            startCol = (x // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[startRow + i][startCol + j] == num:
                        return False

            return True

        def solve(board):


            for y in range(9):
                for x in range(9):

                    if board[y][x] == '.':

                        for num in range(1,10):

                            if is_valid(str(num),x,y,board):

                                board[y][x] = str(num)

                                if solve(board):
                                    return True

                                board[y][x] = '.'

                        return False

            return True
        
        solve(board)