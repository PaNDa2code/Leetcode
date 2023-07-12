class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:


        for y in range(9):
            for x in range(9):
                
                if board[y][x] != '.':
                    
                    # cheak y
                    for i in range(9):

                        if i != y and board[i][x] == board[y][x]:

                            return False
                    # cheak x
                    for i in range(9):

                        if i != x and board[y][i] == board[y][x]:

                            return False

                    # cheak 3x3

                    start_x = x - x % 3
                    start_y = y - y % 3

                    for y2 in range(3):
                        for x2 in range(3):
                            if  (
                            (start_y + y2 != y or start_x + x2 != x)
                            and board[start_y + y2][start_x + x2] == board[y][x]
                        ):
                                return False
                            
        return True
    