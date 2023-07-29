class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:       
        left, right = 0, len(numbers) - 1
        while left <= right:
            val = numbers[left] + numbers[right]            
            if val == target:
                return [left+1,right+1]          
            elif val > target:
                right -= 1
            else:
                left += 1