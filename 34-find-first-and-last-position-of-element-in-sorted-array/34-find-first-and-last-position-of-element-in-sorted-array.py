class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if nums == []:
            return [-1,-1]
        
        if len(nums) == 1:
            if target in nums:
                return [0,0]
            else:
                return [-1,-1]
            
        if len(nums) == 2:
            if target == nums[0] and target == nums[1]:
                return [0, 1]
            elif target == nums[0]:
                return [0, 0]
            elif target == nums[1]:
                return [1, 1]
            else:
                return [-1, -1]
            
        left = 0
        
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (left+right) // 2
            
            if nums[mid] < target:
                
                left = mid + 1
            
            elif nums[mid] > target:
                
                right = mid - 1
            
            else:
                
                break
            
            
        
        if nums[mid] != target:
            return [-1,-1]
        
        # find start and end
        start = mid
        end = mid
        
        while True:
            if start > 0 and nums[start - 1] == target:
                start -= 1
            else:
                break

        while True:
            if end < len(nums) - 1 and nums[end + 1] == target:
                end += 1
            else:
                break

                
                
        
        return [start,end]
            
            