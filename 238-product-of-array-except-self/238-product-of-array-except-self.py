class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        tmp,ziros,sum = [],[],1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                ziros.append(i)
            else:
                sum *= nums[i]
        
        if len(ziros) > 1 or len(ziros) == len(nums):
            return [0]*len(nums)
        
        elif len(ziros) == 1:           
            
            tmp = [0]*len(nums)
            
            tmp[ziros[0]] = sum
            
            return tmp
        else:
            
            for i in range(len(nums)):
                tmp.append((sum//nums[i]))
            return tmp
            
        
            