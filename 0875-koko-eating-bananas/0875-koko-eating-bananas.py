class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            h = 0
            for b in piles:
                h += (b // k) + (b % k > 0)
            return h
        
        left = 1
        right = max(piles)
        
        while left < right:
            
            mid = (left+right)//2
            Th = check(mid)
            
            if Th <= h:
                right = mid
            elif Th > h:
                left = mid + 1
        
        return left
            
            
            
        
        