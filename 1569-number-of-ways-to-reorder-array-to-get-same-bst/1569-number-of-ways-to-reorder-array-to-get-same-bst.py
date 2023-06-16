class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        md = 10 ** 9 + 7
        
        def dfs(nums):
            m = len(nums)
            if m <3:
                return 1
            left = [i for i in nums if i < nums[0]]
            right = [i for i in nums if i > nums[0]]
            return dfs(right) * dfs(left) *  comb(m-1,len(left)) % md
        
        return (dfs(nums)-1) % md
            