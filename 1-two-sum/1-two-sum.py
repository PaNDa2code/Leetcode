class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output = []
        # if not 2 <= len(nums) <= 10 ** 4:
        #     raise ValueError('Too many numpers')
        # if not -10 ** 9 <= target <= 10 ** 9:
        #     raise ValueError('Big target')
        # for i in nums:
        #     if not -10 ** 9 <= i <= 10 ** 9:raise ValueError('Big numpers')
        
        tmp = {}
        
        for i in range(len(nums)):
            num = nums[i]
            lkf = target - num
            if lkf in tmp:
                return [i,tmp[lkf]]
            tmp[num] = i
                
            
            
                     
            
            
            
            
            
            
            
            