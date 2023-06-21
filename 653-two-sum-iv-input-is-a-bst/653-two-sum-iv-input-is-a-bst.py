# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        st = set()
        
        lst = [root]
        
        for node in lst:
            
            if k - node.val in st:return True
            
            st.add(node.val)
            
            if node.left:lst.append(node.left) 
            
            if node.right:lst.append(node.right) 
        
        return False
        