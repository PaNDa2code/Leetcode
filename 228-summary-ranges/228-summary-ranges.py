class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:


        start = 0

        rn = []

        i = 0


        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i]+1 == nums[i+1] :
                i += 1

            if start != nums[i]:
                rn.append('%d->%d'%(start,nums[i]))
            else:
                rn.append(str(nums[i]))
            i += 1

        return rn