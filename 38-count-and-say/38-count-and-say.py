class Solution:
    def countAndSay(self, n: int) -> str:
        
        string = '1'
        
        for _ in range(n-1):
            
            last,tmp,count = string[0] , [] , 0
            
            for num in string:
                
                if num == last:
                    
                    count += 1
                    
                else:
                    
                    tmp.append(f'{count}{last}')
                    
                    count = 1
                    
                    last = num
            
            tmp.append(f'{count}{last}')
            string = ''.join(tmp)

        return string
            
                
            
            