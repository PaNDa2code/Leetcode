# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        cur_level_nodes = [root]
        
        next_level_nodes = []
        
        out = []
        
        while cur_level_nodes != []:
            
            
            for node in cur_level_nodes:
                
                if node.left:
                    
                    next_level_nodes.append(node.left)
                    
                if node.right:
                    
                    next_level_nodes.append(node.right)
                    
            out.append(cur_level_nodes[-1].val)
            
            cur_level_nodes = next_level_nodes
            
            next_level_nodes = []
        
        return out
            
            