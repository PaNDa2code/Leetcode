class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a == b == c:
            return 0
        
        # Calculate the maximum number of digits among a, b, and c
        g = max(len(bin(a)), len(bin(b)), len(bin(c))) + 2
        
        # Convert a, b, c to binary strings of the same length
        a_ = format(a, f'0{g-2}b')
        b_ = format(b, f'0{g-2}b')
        c_ = format(c, f'0{g-2}b')
        
        deff = 0 
        
        for i in range(len(a_)):
            if int(a_[i]) | int(b_[i]) != int(c_[i]):
                if int(a_[i]) & int(b_[i]) == 1 and int(c_[i]) == 0:
                    deff += 2
                else:
                    deff += 1

        return deff
