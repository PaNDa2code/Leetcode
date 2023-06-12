class Solution:
    def maxArea(self, height: list[int]) -> int:

        left,right = 0,len(height)-1

        area = 0

        while left < right:
            area = max(area,(right - left)* min(height[right],height[left]))

            if height[left] < height[right]:

                left += 1

            else:

                right -= 1

        return area