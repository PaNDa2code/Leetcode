import numpy as np

# these is the classic slotion
# Runtime: 120 ms, faster than 28.92% 
# Memory Usage: 57.3 MB, less than 9.78%

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         tmp,zeros,sum = [],[],1
        
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 zeros.append(i)
#             else:
#                 sum *= nums[i]
        
#         if len(zeros) > 1 or len(zeros) == len(nums):
#             return [0]*len(nums)
        
#         elif len(zeros) == 1:           
            
#             tmp = [0]*len(nums)
            
#             tmp[zeros[0]] = sum
            
#             return tmp
#         else:
            
#             for i in range(len(nums)):
#                 tmp.append(sum//nums[i])
                
#             return tmp

# these is just for testing

class Solution:
    def productExceptSelf(self, nums):
        nums = np.array(nums)
        n = len(nums)
        zeros = np.where(nums == 0)[0]

        if len(zeros) > 1 or len(zeros) == n:
            return [0] * n

        elif len(zeros) == 1:
            output = np.zeros(n, dtype=int)
            product = np.prod(nums[np.nonzero(nums)], dtype=int)
            output[zeros[0]] = product
            return output.tolist()

        else:
            product = np.prod(nums, dtype=int)
            output = product // nums
            return output.tolist()

