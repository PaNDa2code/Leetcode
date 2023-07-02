class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        tmp = {}
        
        left = 0
        right = 1
        max_prof = 0
        
        while right < len(prices):
            cur_prof = prices[right] - prices[left]
            
            if prices[left] < prices[right]:
                max_prof = max(max_prof,cur_prof)
            
            else:
                left = right
            right += 1
            
        return max_prof
        
        
            
            
            
        