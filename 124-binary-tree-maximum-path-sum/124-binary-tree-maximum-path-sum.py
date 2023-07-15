# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a global variable to track the maximum path sum
        self.max_sum = float('-inf')

        def helper(node):
            if not node:
                return 0

            # Recursively calculate the maximum sum of left and right subtrees
            left_max = max(helper(node.left), 0)
            right_max = max(helper(node.right), 0)

            # Calculate the current path sum considering node value and maximum sums of left and right subtrees
            cur_sum = node.val + left_max + right_max

            # Update the global maximum sum if the current path sum is greater
            self.max_sum = max(self.max_sum, cur_sum)

            # Return the maximum sum considering the current node and one subtree (left or right)
            return node.val + max(left_max, right_max)

        # Call the helper function to calculate the maximum path sum
        helper(root)

        return self.max_sum