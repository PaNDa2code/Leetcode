def get_mid(ri,le):
    return (ri + le) // 2

class Solution:
    def search(self, nums: list[int], target: int) -> int:

         
        left = 0
        right = len(nums)-1

        if not target in nums:
            return -1

        while left <= right:

            mid = get_mid(left,right)
            mid_f = nums[mid] 

            if mid_f < target:
                left = mid + 1
            elif mid_f > target:
                right = mid - 1
            if mid_f == target:
                return mid 