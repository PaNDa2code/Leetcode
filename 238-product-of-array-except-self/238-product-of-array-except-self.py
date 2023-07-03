# import numpy as np

# these is the classic slotion
# Runtime: 120 ms, faster than 28.92% 
# Memory Usage: 57.3 MB, less than 9.78%

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Compute prefix products
        prefix_product = 1
        for i in range(n):
            output[i] *= prefix_product
            prefix_product *= nums[i]
        
        # Compute suffix products
        suffix_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]
        
        return output


# these is just for testing

# class Solution:
#     def productExceptSelf(self, nums):
#         nums = np.array(nums)
#         n = len(nums)
#         zeros = np.where(nums == 0)[0]

#         if len(zeros) > 1 or len(zeros) == n:
#             return [0] * n

#         elif len(zeros) == 1:
#             output = np.zeros(n, dtype=int)
#             product = np.prod(nums[np.nonzero(nums)], dtype=int)
#             output[zeros[0]] = product
#             return output.tolist()

#         else:
#             product = np.prod(nums, dtype=int)
#             output = product // nums
#             return output.tolist()

