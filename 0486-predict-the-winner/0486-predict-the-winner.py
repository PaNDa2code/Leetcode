class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        
        def deff(left,right):

            if left == right:
                return nums[left]
            left_socre = nums[left] - deff(left+1,right)
            right_score = nums[right] - deff(left,right-1)

            return max(left_socre,right_score)
        

        return deff(0,len(nums)-1) >= 0