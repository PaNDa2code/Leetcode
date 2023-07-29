class Solution:
    def isValid(self, s: str) -> bool:
        stack = []       
        d = {
            
            ')':'(',
            ']':'[',
            '}':'{'
        }       
        for i in s:           
            if i not in d:
                stack.append(i)           
            elif i in d:
                if len(stack) == 0 or stack.pop(-1) != d[i]:
                    return False
        
        return len(stack) == 0