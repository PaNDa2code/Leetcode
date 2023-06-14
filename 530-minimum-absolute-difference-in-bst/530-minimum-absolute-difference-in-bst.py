# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_d = float('inf')
        self.last_v = None

    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return

            dfs(node.left)

            if self.last_v is not None:
                self.min_d = min(self.min_d, abs(node.val - self.last_v))

            self.last_v = node.val

            dfs(node.right)

        dfs(root)

        return self.min_d

        