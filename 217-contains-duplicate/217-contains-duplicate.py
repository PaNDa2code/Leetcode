class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        tmp = {}
        
        for num in nums:
            
            if tmp.get(num,0) == 1:
                return True
            tmp[num] = tmp.get(num,0) + 1
            
        return False