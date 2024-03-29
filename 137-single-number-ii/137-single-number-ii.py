class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0  # Tracks the bits that appear once
        twos = 0  # Tracks the bits that appear twice or more
        
        for num in nums:
            ones = ~twos & (ones^num)
            twos = ~ones & (twos^num)
        return ones
    