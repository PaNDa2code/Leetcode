class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        curant_sum = sum(nums[0:3])

        nums = sorted(nums)

        for i in range(len(nums)):

            left = i + 1

            right = len(nums)-1

            while left < right:

                su = sum((nums[left],nums[right],nums[i]))

                if abs(curant_sum - target) > abs(su - target):

                    curant_sum = su

                if su < target:
                    left += 1

                elif su > target:
                    right -= 1
                    
                else:
                    
                    break


        return curant_sum