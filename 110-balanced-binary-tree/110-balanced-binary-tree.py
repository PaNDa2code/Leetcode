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
                return True
            
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                return False
            else:
                return check(root.left) and check(root.right)
            
        def height(root):
            if root:
                return 1 + max(height(root.left), height(root.right))
            else:
                return 0

        return check(root)


        
            
        