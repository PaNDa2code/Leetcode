class Solution:
	def sortArray(self, nums: list[int]) -> list[int]:
		
		hashmap = {}
		min_val , max_val = min(nums) , max(nums)
		# counting hashmap
		for i in nums:
			hashmap[i] = hashmap.get(i,0) + 1
			
		x = 0
		for i in range(min_val,max_val+1):
			
			while hashmap.get(i,0)>0:
				nums[x] = i
				x += 1
				hashmap[i] -= 1
				
		return nums