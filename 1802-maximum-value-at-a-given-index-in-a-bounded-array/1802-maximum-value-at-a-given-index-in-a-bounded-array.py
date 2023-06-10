# def arr(n):
#     return [1]*n

# def increment_slice(array, x, index,max):


    

#     if index == len(array)-1:

#         for i in range(index-x, index+1):
#             if i < 0 or i+1 > len(array):continue
#             array[i] += 1


#     else:

#         for i in range(index - x, x + index+1):
#             if i < 0 or i+1 > len(array):continue            
#             array[i] += 1


# class Solution:
    # def maxValue(self, n: int, index: int, maxSum: int) -> int:

#         array = arr(n)

#         x = 0 

#         end  = False

#         while not end:

#             old_array = array.copy()

#             # if sum(array)+n*2 > maxSum:
#                 # end = True

#             increment_slice(array,x,index,maxSum)

#             if sum(array)> maxSum:
#                 end = True
#                 array = old_array

#             x += 1

#         print(array)

#         return max(array)

# working but bad
# so i ll use binary search
class Solution:
    def maxValue(self, n, index, maxSum):
        def test(mid):
            b = max(mid - index, 0)
            res = (mid + b) * (mid - b + 1) // 2
            b = max(mid - ((n - 1) - index), 0)
            res += (mid + b) * (mid - b + 1) // 2
            return res - mid

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1
