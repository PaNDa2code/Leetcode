class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        hashmap = {}
        max_length = 0
        for i in range(len(nums)):
            hashmap[nums[i]] = {}
            for j in range(i):
                diff = nums[i] - nums[j]
                hashmap[nums[i]][diff] = hashmap[nums[j]].get(diff, 1) + 1
                max_length = max(max_length, hashmap[nums[i]][diff])
        return max_length


