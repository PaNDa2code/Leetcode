class Solution:
    def countBits(self, n: int) -> list[int]:
        
        dp, offcet = [0]*(n+1), 1
        for i in range(1,n+1):
            offcet = i if offcet * 2 == i else offcet
            dp[i] = 1 + dp[i-offcet]
        return dp