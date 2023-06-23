# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def tre(node):
            if node:
                return [node.val] + tre(node.left) + tre(node.right)
            else:
                return ['null']
        
        return tre(p) == tre(q)
            
            