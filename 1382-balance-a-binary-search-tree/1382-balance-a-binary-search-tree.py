# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_list = self.inorderTraversal(root)
        return self.constructAVL(sorted_list, 0, len(sorted_list) - 1)
    
    def inorderTraversal(self, node: TreeNode) -> List[int]:
        if not node:
            return []
        return self.inorderTraversal(node.left) + [node.val] + self.inorderTraversal(node.right)
    
    def constructAVL(self, sorted_list: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(sorted_list[mid])
        
        root.left = self.constructAVL(sorted_list, left, mid - 1)
        root.right = self.constructAVL(sorted_list, mid + 1, right)
        
        return root

            
        
            
        