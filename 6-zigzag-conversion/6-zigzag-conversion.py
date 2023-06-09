class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:return s

        output = ''

        for x in range(numRows):
            jump_0 = (numRows-1)*2 
            for y in range(x,len(s),jump_0):
                output += s[y]
                if x != 0 and x != numRows - 1 and y + jump_0 - 2 * x < len(s):
                    output += s[y + jump_0 - 2 * x]
        return output