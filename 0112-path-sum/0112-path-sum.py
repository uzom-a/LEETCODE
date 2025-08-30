# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False
            
            if node.left == None and node.right == None:
                return curr + node.val == targetSum

            curr += node.val #keeping track of a running sum
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right #if one path is True return it that is why we used the or

        return dfs(root, 0)
#Soace and Time Complexity is both O(n)