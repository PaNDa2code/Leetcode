class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num,0) + 1
        
        bucket = [ [] for _ in range(len(nums))]
        
        for num in counter:            
            index = counter[num]-1
            bucket[index].append(num)

        out = [item for i in bucket for item in i][::-1][:k]

        return out