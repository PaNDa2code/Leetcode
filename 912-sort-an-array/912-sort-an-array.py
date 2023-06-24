def merge(nums1,nums2):
    
    out = []
    x,y = 0,0
    
    while x < len(nums1) and y < len(nums2):
        if nums1[x] <= nums2[y]:
            out.append(nums1[x])
            x += 1
        else:
            out.append(nums2[y])
            y += 1
            
    return out + nums1[x:] + nums2[y:]

def merge_sort(nums):
    
    if len(nums)<= 1:
        
        return nums
    
    mid = len(nums) // 2
    
    left , right = nums[:mid] , nums[mid:]
    
    left_sorted , right_sorted = merge_sort(left) , merge_sort(right)
    
    return merge(left_sorted,right_sorted)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)