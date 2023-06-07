class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1
        nums.extend(nums2)
        nums = sorted(nums)

        x = len(nums)

        if x % 2 != 0:
            return nums[x//2]
        else:
            return (nums[x//2]+nums[(x-1)//2]) / 2