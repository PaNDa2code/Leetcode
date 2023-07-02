class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof = 0
        sml_valu = prices[0]
        
        for i in range(1,len(prices)):
            sml_valu = min(sml_valu,prices[i])
            max_prof = max(max_prof,prices[i]-sml_valu)
            
        return max_prof
        
        
            
            
            
        