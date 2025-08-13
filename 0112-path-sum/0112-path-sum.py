# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node: #if the tree is empty
                return False

            if node.left == None and node.right == None: #that means we are at a leaf node
                return (curr + node.val) == targetSum

            curr += node.val
            print(curr)
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right #because we just need to find any path that sums up to the targetSum

        return dfs(root, 0) #intialize curr to 0 

        # Space Complexity = O(n)
        # Time Complexity = O(n)