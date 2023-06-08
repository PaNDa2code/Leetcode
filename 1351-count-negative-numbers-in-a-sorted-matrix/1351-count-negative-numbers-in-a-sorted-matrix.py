class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        neg = 0
        for x in grid:
            for y in x:
                if y < 0 :
                    neg+=1
        return neg