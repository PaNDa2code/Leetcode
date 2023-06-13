import collections

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        out = 0
        
        dic = collections.Counter((tuple(r) for r in grid))

        for c in range(len(grid)):

            cc = tuple(grid[i][c] for i in range(len(grid)))

            out += dic[cc]

        return out