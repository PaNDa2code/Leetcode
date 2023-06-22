# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def sortedtrav(node):
            
            if node:
                return sortedtrav(node.left)+[node.val]+sortedtrav(node.right)
            else:
                return []
        
        def bst(lis,left,right):

            if not lis:
                return 
            
            left = 0
            right= len(lis)-1
            
            mid  = (left + right) // 2
            
            root = TreeNode(lis[mid])
            root.left = bst(lis[:mid],left,mid - 1)
            root.right= bst(lis[mid+1:],mid + 1,right)
            
            return root
        
        sorted = sortedtrav(root)

        return bst(sorted,0,len(sorted)-1)
            
            
            
        
            
        