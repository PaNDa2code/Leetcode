class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0 
        
        # n ^ 0 = n
        # n ^ n = 0
        
        # so if num is not showed before __ n = num
        
        # if n is showed before __ n = 0
        
        for num in nums:
            n ^= num
       
        return n
