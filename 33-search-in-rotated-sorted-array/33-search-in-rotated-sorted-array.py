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

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] == target:
                return mid_pivot
            elif nums[mid_pivot] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        
        
        
        

#         if target not in nums:
#             return -1
#         if len(nums) == 1:
#             return 0
        
#         return nums.index(target)
#         # left = 0
#         # right= len(nums)-1

# #         while left <= right:
# #             mid = (left+right)//2

# #             if target == nums[mid]:
# #                 return mid
    

# #             if nums[left] <= nums[mid]:
# #                 if nums[left]<=target<=nums[mid]:
# #                     right = mid - 1
# #                 else:
# #                     left = mid + 1
# #             else:
# #                 if nums[mid]<=target<=nums[right]:
# #                     left = mid + 1
# #                 else:
# #                     right = mid - 1
