class Solution:
    
    
    
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x,-n)
        
        isOdd = lambda x: x % 2 != 0
        
        if isOdd(n):
            
            return x * self.myPow(x*x, (n-1) // 2)
        
        else:
            
            return self.myPow(x*x, n // 2)
        
        
        
        
        