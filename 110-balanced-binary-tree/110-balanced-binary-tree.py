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
                return 0, True
            
            
            left_hight , left_balanced = check(root.left)
            
            #early cheak to reduse times of trys
            if not left_balanced:
                return -1, False
             
            right_hight , right_balanced = check(root.right)
            
            if not right_balanced:
                return -1, False
            
            node_hight = 1 + max(left_hight,right_hight)
            
            is_b = abs(right_hight - left_hight) <= 1
            
            return node_hight, is_b

        return check(root)[1]
      