# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def tre(node1):
            if node1:
                return [node1.val] + tre(node1.left) + tre(node1.right)
            else:
                return ['null']
        
        return tre(p) == tre(q)
            
            