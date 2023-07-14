class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in range(len(matrix)):
            
            if matrix[m][-1] == target:
                
                return True
            
            elif matrix[m][-1] > target:
                
                left = 0
                
                right = len(matrix[m]) - 1
                
                while left <= right:
                    
                    mid = (left+right) // 2
                    
                    if matrix[m][mid] == target:
                        
                        return True
                    
                    elif matrix[m][mid] > target:
                        
                        right = mid - 1
                        
                    else:
                        
                        left = mid + 1
                    
                    
            
            
        return False