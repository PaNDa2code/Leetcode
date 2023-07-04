class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target not in nums:
            return -1
        
        def find_pivot(lst):
            left = 0
            right = len(lst) - 1

            while left < right:
                mid = (left + right) // 2

                if lst[mid] > lst[right]:
                    left = mid + 1
                else:
                    right = mid

            return left

                

        pivot = find_pivot(nums)
        # print(pivot)

        def find_target(lst,t):
            
            left = 0
            
            right = len(lst) -1
            
            while left <= right:
                
                mid = (left + right) // 2
                
                if lst[mid] > t:
                    right = mid - 1
                elif lst[mid] == t:
                    return mid
                else:
                    left = mid + 1
                
            return left
        
        return (find_target(nums[pivot:]+nums[:pivot+1],target) + pivot) % len(nums)
            
                    
                    
                
                
            
        

