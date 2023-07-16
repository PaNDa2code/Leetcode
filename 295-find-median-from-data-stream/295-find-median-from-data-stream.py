class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        
        left = 0
        right = len(self.arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.arr[mid] <= num:
                left = mid + 1
            elif self.arr[mid] > num:
                right = mid - 1

        self.arr.insert(left, num)
        
    def findMedian(self) -> float:
        
        mid = (len(self.arr)-1) // 2
        
        if len(self.arr) % 2 == 1:
            
            return self.arr[mid]
        
        else:
            
            return (self.arr[mid] + self.arr[mid+1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()