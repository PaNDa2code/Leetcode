class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        # O(n)
        for num in nums:

            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:

                # binary search
                # O(log n)

                left = 0
                right = len(sub)-1

                while left <= right:
                    mid = (left+right)//2
                    if sub[mid] < num:
                        left = mid +1
                    else:
                        right = mid -1


                idx = left
                sub[idx] = num
                
        return len(sub)