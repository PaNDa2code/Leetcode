def insert(arr,value):
    
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= value:
            left = mid + 1
        elif arr[mid] > value:
            right = mid - 1
    
    arr.insert(left, value)
            
        
    
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        
        insert(self.arr,num)

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