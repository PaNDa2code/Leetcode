class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        dp = [{} for _ in range(n)]
        max_length = 2
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                max_length = max(max_length, dp[i][diff])
        
        return max_length
