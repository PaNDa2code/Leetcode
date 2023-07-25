class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:        
        left, right = 0, len(arr) - 1
        getMid = lambda l, r: (l + r) // 2
        while left <= right:
            mid = getMid(left, right)
            if arr[mid] > arr[mid + 1]:
                if arr[mid - 1] < arr[mid]:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return left