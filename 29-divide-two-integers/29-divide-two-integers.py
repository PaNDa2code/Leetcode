class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        counter = 0
        sign = 1
        
        if divisor == 0:
            return
        if divisor < 0:
            sign *= -1
            divisor = abs(divisor)
        if dividend < 0:
            sign *= -1
            dividend = abs(dividend)
        
        out = 0
        if divisor == 1:
            out = dividend * sign       
            
        else:
            
            out = len(range(0, dividend - divisor + 1, divisor))*sign

        if out > 2147483647:
            return 2147483647
        elif out < -2147483648:
            return -2147483648
        else:
            return out