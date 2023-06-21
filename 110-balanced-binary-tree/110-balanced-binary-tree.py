# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def check(root):
            
            if root is None:
                return 0
            
            left_hight = check(root.left)
            
            if left_hight == -1:
                return -1
             
            right_hight = check(root.right)
            
            if right_hight == -1:
                return -1
            
            
            if abs(right_hight - left_hight) > 1:
                return -1
            
            return 1 + max(left_hight,right_hight)

        return check(root) != -1
      