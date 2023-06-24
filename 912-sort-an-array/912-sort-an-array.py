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

def counting_sort(nums):
	
	count = {}
	
	min_val , max_val = min(nums) , max(nums)
	
	for i in nums:
		count[i] = count.get(i,0) + 1
	x = 0
	for i in range(min_val,max_val+1):
		while count[i] > 0:
			nums[x] = i
			x += 1
			count[i] -= 1
                        
	return nums

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if max(nums) - min(nums) <= 2: return counting_sort(nums)
        return merge_sort(nums)	