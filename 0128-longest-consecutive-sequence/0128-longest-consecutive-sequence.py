class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        Set = set(nums)
        
        maxsq = 0
        
        for num in nums: 
            if not num - 1 in Set:
                sq = 1
                while num + sq in Set:
                    sq+=1
                maxsq = max(maxsq,sq)
                
        return maxsq
            
            
            
        
                
        
        